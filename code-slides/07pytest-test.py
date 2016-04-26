import pytest
from selenium.webdriver import Firefox

#!
@pytest.fixture
#!
def driver():
    return Firefox()
#!
def test_github_search(driver):
    driver.get('https://github.com')
    search_box = driver.find_element_by_name('q')
    search_box.send_keys('txtorcon')
    search_box.submit()
#!
    found_repos = [
        repo.text for repo in
        driver.find_elements_by_class_name('repo-list-name')
    ]
#!
    assert 'meejah/txtorcon' in found_repos
