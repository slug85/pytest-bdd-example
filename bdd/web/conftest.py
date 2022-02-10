import pytest
import selene.browser
from _pytest.fixtures import FixtureRequest
from selene import config
from selene.factory import get_shared_driver


@pytest.fixture(scope="session")
def config_browser(request: FixtureRequest):
    base_url = request.config.getoption("--url")
    config.base_url = base_url
    config.timeout = 20


@pytest.fixture(autouse=True)
def close_browser():
    yield
    if get_shared_driver():
        selene.browser.quit()
