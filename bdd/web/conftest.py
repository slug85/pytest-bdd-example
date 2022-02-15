import pytest
import selene.browser
from _pytest.fixtures import FixtureRequest
from selene import config


@pytest.fixture(scope="session", autouse=True)
def config_browser(request: FixtureRequest):
    base_url = request.config.getoption("--url")
    config.base_url = base_url
    config.timeout = 20
    yield


@pytest.fixture(autouse=True)
def close_browser():
    yield
    selene.browser.quit()
