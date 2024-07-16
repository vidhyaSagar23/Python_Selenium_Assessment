import pytest

from page_objects.HomePage import HomePage
from test_data.TestData import TestData
from utilities.BaseClass import BaseClass


class TestThree(BaseClass):
    def test_incorrect_email_password(self):
        log = self.getLogger()
        home_page = HomePage(self.driver)
        data = TestData()
        assert home_page.verify_home_page().is_displayed()
        log.info("Home page displayed")
        login_page = home_page.click_login_btn()
        assert data.login_text in login_page.login_to_account_text()
        login_page.enter_login_details()
        assert data.incorrect_validate in login_page.validate_error_message()
        log.info("Error message shown")
