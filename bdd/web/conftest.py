import pytest
import selene.browser
from _pytest.fixtures import FixtureRequest
from selene import config, browser
from selenium import webdriver


@pytest.fixture(scope="session", autouse=True)
def config_browser(request: FixtureRequest):
    base_url = request.config.getoption("--url")
    config.base_url = base_url
    config.timeout = 20

    driver = webdriver.Remote(
        command_executor='http://selenosis.selenosis-dev.svc.k8s-test.dataspace:8080/wd/hub',
        desired_capabilities={'browserName': 'chrome',
                              'enableVNC': True,
                              'javascriptEnabled': True})

    browser.set_driver(driver)
    yield


@pytest.fixture(autouse=True)
def close_browser():
    yield
    selene.browser.quit()
