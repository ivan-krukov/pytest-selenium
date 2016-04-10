import pytest


def pytest_addoption(parser):
    # must add --slow to run any tests marked @pytest.mark.slowtest
    parser.addoption(
        "--slow", action="store_true", dest="slow",
        help="Turn on any tests decorated with @pytest.mark.slowtest"
    )


def pytest_runtest_setup(item):
    # look for tests with @pytest.mark.slowtest on them and turn them
    # off (unless --slow was passed)
    slowmark = item.get_marker('slowtest')
    if slowmark is not None:
        if not item.config.getoption('slow', False):
            pytest.skip("pass --slow to run this test")
