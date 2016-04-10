from __future__ import print_function

from time import sleep
from selenium.webdriver import Firefox, Chrome
import pytest


@pytest.fixture(
    scope='session',
    params=['firefox', 'chrome'],
)
def driver(request):
    browser = request.param
    if browser == 'firefox':
        driver = Firefox()
    elif browser == 'chrome':
        driver = Chrome()
    else:
        raise ValueError("Unknown browser '{}'".format(browser))
    request.addfinalizer(lambda: driver.quit())
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
