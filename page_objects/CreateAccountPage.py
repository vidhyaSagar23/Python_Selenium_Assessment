from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from page_objects.ConfirmationPage import ConfirmationPage


class CreateAccountPage:
    def __init__(self, driver):
        self.driver = driver

    verify_createAccountPage_isvisible = (By.CSS_SELECTOR, "h2:nth-child(1) b")
    gender = (By.ID, "id_gender1")
    password = (By.ID, "password")
    days = (By.ID, "days")
    months = (By.ID, "months")
    years = (By.ID, "years")
    newsletter_checkbox = (By.XPATH, "//label[@for='newsletter']")
    optin_checkbox = (By.XPATH, "//label[@for='optin']")
    first_name = (By.ID, "first_name")
    last_name = (By.ID, "last_name")
    company = (By.ID, "company")
    address = (By.ID, "address1")
    countries = (By.ID, "country")
    state = (By.CSS_SELECTOR, "[name='state']")
    city = (By.ID, "city")
    zip = (By.ID, "zipcode")
    mobile = (By.ID, "mobile_number")
    create_account_btn = (By.XPATH, "//button[text()='Create Account']")

    def verify_createAccountPage(self):
        return self.driver.find_element(*CreateAccountPage.verify_createAccountPage_isvisible).is_displayed()

    def enterDetails(self):
        self.driver.find_element(*CreateAccountPage.gender).click()
        self.driver.find_element(*CreateAccountPage.password).send_keys("sagar")
        Select(self.driver.find_element(*CreateAccountPage.days)).select_by_visible_text("13")
        Select(self.driver.find_element(*CreateAccountPage.months)).select_by_visible_text("August")
        Select(self.driver.find_element(*CreateAccountPage.years)).select_by_visible_text("2001")
        self.driver.find_element(*CreateAccountPage.newsletter_checkbox).click()
        self.driver.find_element(*CreateAccountPage.optin_checkbox).click()

    def enterAddressDetails(self):
        self.driver.find_element(*CreateAccountPage.first_name).send_keys("sagar")
        self.driver.find_element(*CreateAccountPage.last_name).send_keys("vp")
        self.driver.find_element(*CreateAccountPage.company).send_keys("qapio")
        self.driver.find_element(*CreateAccountPage.address).send_keys("karuppur")
        Select(self.driver.find_element(*CreateAccountPage.countries)).select_by_visible_text("India")
        self.driver.find_element(*CreateAccountPage.state).send_keys("Tamil Nadu")
        self.driver.find_element(*CreateAccountPage.city).send_keys("salem")
        self.driver.find_element(*CreateAccountPage.zip).send_keys("636012")
        self.driver.find_element(*CreateAccountPage.mobile).send_keys("9344508181")
        self.driver.find_element(*CreateAccountPage.create_account_btn).click()
        return ConfirmationPage(self.driver)


