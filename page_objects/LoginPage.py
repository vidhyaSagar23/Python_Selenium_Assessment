from selenium.webdriver.common.by import By

from page_objects.CreateAccountPage import CreateAccountPage
from test_data.TestData import TestData


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.data = TestData()

    signup_text = (By.CSS_SELECTOR, "div[class='signup-form'] h2")
    username = (By.CSS_SELECTOR, "div[class='signup-form'] input[name='name']")
    email = (By.CSS_SELECTOR, "div[class='signup-form'] input[name='email']")
    submit_btn = (By.CSS_SELECTOR, "div[class='signup-form'] button[type='submit']")

    login_title_text = (By.XPATH, "//h2[text()='Login to your account']")
    login_email = (By.CSS_SELECTOR, "input[data-qa='login-email']")
    login_password = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    login_btn = (By.CSS_SELECTOR, "button[data-qa='login-button']")

    error_message = (By.XPATH, "//p[text()='Your email or password is incorrect!']")

    def verify_Account_Information_visible(self):
        return self.driver.find_element(*LoginPage.signup_text).is_displayed()

    def enterSignUpDetails(self):
        self.driver.find_element(*LoginPage.username).send_keys(self.data.user_name)
        self.driver.find_element(*LoginPage.email).send_keys(self.data.email)
        self.driver.find_element(*LoginPage.submit_btn).click()
        return CreateAccountPage(self.driver)

    def login_to_account_text(self):
        return self.driver.find_element(*LoginPage.login_title_text).text

    def enter_login_details(self):
        self.driver.find_element(*LoginPage.login_email).send_keys(self.data.login_email)
        self.driver.find_element(*LoginPage.login_password).send_keys(self.data.login_password)
        self.driver.find_element(*LoginPage.login_btn).click()

    def validate_error_message(self):
        return self.driver.find_element(*LoginPage.error_message).text
