from __future__ import print_function

from time import sleep
from selenium.webdriver import Firefox, Chrome
import pytest


@pytest.fixture(
    scope='session',
    params=[
        'firefox',
        pytest.mark.skip('not using chrome')('chrome'),
    ],
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
    if 'torproject' in url and isinstance(driver, Chrome):
        pytest.skip("not visiting '{}' in Chrome".format(url))
    request.addfinalizer(lambda: driver.get(old_url))
    driver.get(url)
    return url


def _test_visit_page(page):
    print("visited", page)
    sleep(2)


@pytest.mark.parametrize(
    'who',
    ('thing one', 'thing two')
)
@pytest.mark.parametrize(
    'what',
    ('cat', 'hat', 'bat')
)
def test_something_else(who, what):
    print("something else: {}, {}".format(who, what))
    assert 'thing' in who
