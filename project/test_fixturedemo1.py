from __future__ import print_function

from time import sleep
from selenium.webdriver import Firefox
import pytest


@pytest.fixture(scope='session')
def driver(request):
    driver = Firefox()
    request.addfinalizer(lambda: driver.quit())
    return driver


@pytest.fixture
def page(request, driver):
    url = 'https://google.com'
    old_url = driver.current_url
    request.addfinalizer(lambda: driver.get(old_url))
    driver.get(url)
    return url


def test_visit_page(page):
    print("visited", page)
    sleep(2)


def test_something_else(driver):
    pass
