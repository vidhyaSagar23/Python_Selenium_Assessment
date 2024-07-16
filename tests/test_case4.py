import logging

import pytest

from page_objects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestFour(BaseClass):
    def test_add_products(self):
        log = self.getLogger()
        home_page = HomePage(self.driver)
        assert home_page.verify_home_page().is_displayed()
        log.info("Home page is displayed")
        products = home_page.click_products_btn()
        products.select_first_product()
        products.click_continue()
        products.select_second_product()
        log.info("Two products have added to cart")
        view_cart = products.click_view_cart()
        view_cart.checkProductIsVisible()
        view_cart.verify_quantity()
        view_cart.verify_total()
