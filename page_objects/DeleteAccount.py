from selenium.webdriver.common.by import By


class DeleteAccount:
    def __init__(self, driver):
        self.driver = driver

    delete_msg = (By.XPATH, "//b[text()='Account Deleted!']")
    continue_btn = (By.XPATH, "//a[@class='btn btn-primary']")

    def validate_delete_msg(self):
        return self.driver.find_element(*DeleteAccount.delete_msg).text

    def clickContinue(self):
        self.driver.find_element(*DeleteAccount.continue_btn).click()
