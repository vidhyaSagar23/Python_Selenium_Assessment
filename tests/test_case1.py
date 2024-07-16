import time

from page_objects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_demo1(self):
        home_page = HomePage(self.driver)
        assert home_page.verify_home_page().is_displayed()
        login_page = home_page.click_login_btn()

        assert login_page.verify_Account_Information_visible()
        create_account_page = login_page.enterSignUpDetails()
        assert create_account_page.verify_createAccountPage()
        create_account_page.enterDetails()
        confirmation_page = create_account_page.enterAddressDetails()
        assert "CREATED" in confirmation_page.validate_created()
        confirmation_page.click_continue()
        assert "sagar" in home_page.validate_login_text()
        delete_account = home_page.click_delete_btn()
        assert "DELETED" in delete_account.validate_delete_msg()
        delete_account.clickContinue()

        time.sleep(4)
        print("success")

    def test_login_with_correct_data(self):
        home_page = HomePage(self.driver)
        assert home_page.verify_home_page().is_displayed()
        login_page = home_page.click_login_btn()
        assert "Login" in login_page.login_to_account_text()
        login_page.enter_login_details()
        assert "sagar" in home_page.validate_login_text()
        delete_account = home_page.click_delete_btn()
        assert "DELETED" in delete_account.validate_delete_msg()
        delete_account.clickContinue()

    def test_incorrect_email_password(self):
        home_page = HomePage(self.driver)
        assert home_page.verify_home_page().is_displayed()
        login_page = home_page.click_login_btn()
        assert "Login" in login_page.login_to_account_text()
        login_page.enter_login_details()
        assert "incorrect" in login_page.validate_error_message()

    def test_add_products(self):
        home_page = HomePage(self.driver)
        assert home_page.verify_home_page().is_displayed()
        products = home_page.click_products_btn()
        products.select_first_product()
        products.click_continue()
        products.select_second_product()
        view_cart = products.click_view_cart()
        view_cart.checkProductIsVisible()
        view_cart.verify_quantity()
        view_cart.verify_total()
        time.sleep(5)


