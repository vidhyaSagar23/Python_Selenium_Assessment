from page_objects.HomePage import HomePage
from test_data.TestData import TestData
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_createAccountAndDelete(self):
        log = self.getLogger()
        home_page = HomePage(self.driver)
        data = TestData()
        assert home_page.verify_home_page().is_displayed()
        log.info("Home Page is visible")
        login_page = home_page.click_login_btn()

        assert login_page.verify_Account_Information_visible()
        log.info("account information text is visible")
        create_account_page = login_page.enterSignUpDetails()
        assert create_account_page.verify_createAccountPage()
        create_account_page.enterDetails()
        confirmation_page = create_account_page.enterAddressDetails()
        assert data.account_created_message in confirmation_page.validate_created()
        log.info("Account created successfully")
        confirmation_page.click_continue()
        assert data.user_name_validate in home_page.validate_login_text()
        delete_account = home_page.click_delete_btn()
        assert data.delete_message in delete_account.validate_delete_msg()
        delete_account.clickContinue()
        log.info("Account deleted successfully")






