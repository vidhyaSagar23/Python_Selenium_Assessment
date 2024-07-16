from selenium.webdriver.common.by import By


class ConfirmationPage:
    def __init__(self, driver):
        self.driver = driver

    account_created_text = (By.XPATH, "//b[text()='Account Created!']")
    continue_btn = (By.XPATH, "//div[@class='pull-right']/a")

    def validate_created(self):
        return self.driver.find_element(*ConfirmationPage.account_created_text).text

    def click_continue(self):
        self.driver.find_element(*ConfirmationPage.continue_btn).click()
