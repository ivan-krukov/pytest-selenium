import pytest
from selenium.webdriver import Firefox
#!
@pytest.fixture(scope='session')
#!
def driver(request):
#!
    driver = Firefox()
#!
    request.addfinalizer(lambda: driver.quit())
#!
    return driver
