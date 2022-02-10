from pytest_bdd import scenario, given
from selene import browser

from datastore import DataStore


@scenario(feature_name="web/web_auth.feature", scenario_name="Открытие формы", features_base_dir="../features")
def test_auth(datastore: DataStore, config_browser):
    open_main_page(datastore)


@given("Я открываю главную страницу")
def open_main_page(datastore: DataStore):
    browser.open_url("/login")
