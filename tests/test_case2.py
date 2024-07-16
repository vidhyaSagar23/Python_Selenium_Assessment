import pytest

from page_objects.HomePage import HomePage
from test_data.TestData import TestData
from utilities.BaseClass import BaseClass


class TestTwo(BaseClass):
    def test_login_with_correct_data(self):
        log = self.getLogger()
        home_page = HomePage(self.driver)
        data = TestData()
        assert home_page.verify_home_page().is_displayed()
        log.info("HomePage is displayed")
        login_page = home_page.click_login_btn()
        assert data.login_text in login_page.login_to_account_text()
        login_page.enter_login_details()
        assert data.user_name_validate in home_page.validate_login_text()
        log.info("Logged in successfully")
        delete_account = home_page.click_delete_btn()
        assert data.delete_message in delete_account.validate_delete_msg()
        log.info("Account deleted successfully")
        delete_account.clickContinue()
