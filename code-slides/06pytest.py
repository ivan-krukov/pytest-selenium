import pytest
from selenium.webdriver import Firefox


#!
@pytest.fixture(scope='session')
#!
def driver(request):
#!
    return Firefox()
