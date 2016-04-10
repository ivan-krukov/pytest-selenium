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
    driver = Firefox()
    request.addfinalizer(lambda: driver.quit())
    return driver


def test_something(driver):
    driver.get('https://google.com')


@pytest.mark.slowtest
def test_something_slow(driver):
    driver.get('https://maps.google.com')
    sleep(10)
