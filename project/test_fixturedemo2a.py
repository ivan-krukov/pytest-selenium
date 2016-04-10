from __future__ import print_function

from time import sleep
from selenium.webdriver import Firefox, Chrome
import pytest


@pytest.fixture(
    scope='session',
    params=[Firefox, Chrome],
)
def driver(request):
    browser_klass = request.param
    driver = browser_klass()
    request.addfinalizer(driver.quit)
    return driver


@pytest.fixture(
    params=[
        'https://torproject.org',
        'https://meejah.ca/projects',
    ]
)
def page(request, driver):
    old_url = driver.current_url
    url = request.param
    request.addfinalizer(lambda: driver.get(old_url))
    driver.get(url)
    return url


def test_visit_page(page):
    print("visited", page)
    sleep(2)


def test_something_else(driver):
    pass
