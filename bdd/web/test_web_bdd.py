from pytest_bdd import scenario, given
from selene import browser

from datastore import DataStore


@scenario(feature_name="web_auth.feature", scenario_name="Открытие формы")
def test_auth(datastore: DataStore, config_browser):
    pass


@given("Я открываю главную страницу")
def open_main_page(datastore: DataStore):
    browser.open_url("/login")
