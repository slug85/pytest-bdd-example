from pytest_bdd import given
from bdd.web.page_objects.catalog_page import CatalogPage
from selene import browser
from datastore import DataStore


@given("Я открываю главную страницу")
def open_main_page(datastore: DataStore):
    browser.open_url("/")


@given("Я открываю каталог")
def open_catalog(datastore: DataStore):
    CatalogPage.open()


@given("Я проверяю товары в каталоге")
def open_catalog(datastore: DataStore):
    CatalogPage.check_catalog()
