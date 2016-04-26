from time import sleep
import pytest
from selenium.webdriver import Firefox
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(scope='session')
def driver(request):
    ff = Firefox()

    def cleanup():
        sleep(2)  # for demo purposes
        ff.quit()
    request.addfinalizer(cleanup)  # or: request.addfinalizer(driver.quit)
    return ff


def test_github_search(driver):
    driver.get('https://github.com')
    search_box = driver.find_element_by_name('q')
    search_box.send_keys('txtorcon')
    search_box.submit()

    found_repos = [
        repo.text for repo in
        driver.find_elements_by_class_name('repo-list-name')
    ]

    assert 'meejah/txtorcon' in found_repos


def test_github_project(driver):
    driver.get('https://github.com/meejah/txtorcon')

    body = driver.find_element_by_tag_name('body')

    # activate the "file finder"
    ActionChains(driver) \
        .move_to_element(body) \
        .click(on_element=body) \
        .send_keys_to_element(body, 't') \
        .perform()

    # wait up to 5 seconds until it's "actually" activated (which we
    # know because an element with a particular ID will be visible)
    finder = WebDriverWait(driver, timeout=5.0).until(
        EC.presence_of_element_located(
            (By.ID, "tree-finder-field")
        )
    )

    # now we press "down" three times, and return...
    ActionChains(driver) \
        .send_keys_to_element(finder, Keys.ARROW_DOWN) \
        .send_keys_to_element(finder, Keys.ARROW_DOWN) \
        .send_keys_to_element(finder, Keys.ARROW_DOWN) \
        .send_keys_to_element(finder, Keys.ENTER) \
        .perform()

    # ...which we confirm because this "should" have loaded the Dockerfile
    WebDriverWait(driver, 5.0).until(EC.title_contains('Dockerfile'))
