from selene.support.jquery_style_selectors import ss
from selene import browser, by, be, have
from selene.conditions import visible


class CatalogPage(object):

    products = ss("div.xf-product__delivery")

    @classmethod
    def check_catalog(cls):
        cls.products.filter(visible).should(have.size_at_least(20))

    @staticmethod
    def open():
        browser.open_url("catalog/1304/ryba-i-moreprodukty")
