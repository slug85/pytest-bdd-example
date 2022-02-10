from pytest_bdd import scenario, given
from bdd.web.ui.catalog_page import CatalogPage
from selene import browser
from datastore import DataStore


@scenario(feature_name="web.feature", scenario_name="Открытие формы")
def test_auth(datastore: DataStore, config_browser):
    pass


@scenario(feature_name="web.feature", scenario_name="Открытие каталога")
def test_catalog(datastore: DataStore, config_browser):
    pass


@given("Я открываю главную страницу")
def open_main_page(datastore: DataStore):
    browser.open_url("/login")


@given("Я открываю каталог")
def open_catalog(datastore: DataStore):
    CatalogPage.open()


@given("Я проверяю товары в каталоге")
def open_catalog(datastore: DataStore):
    CatalogPage.check_catalog()
