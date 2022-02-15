from pytest_bdd import given
from bdd.web.ui.catalog_page import CatalogPage
from selene import browser
from datastore import DataStore


@given("Я открываю главную страницу")
def open_main_page(datastore: DataStore):
    browser.open_url("/login")


@given("Я открываю каталог")
def open_catalog(datastore: DataStore):
    CatalogPage.open()


@given("Я проверяю товары в каталоге")
def open_catalog(datastore: DataStore):
    CatalogPage.check_catalog()