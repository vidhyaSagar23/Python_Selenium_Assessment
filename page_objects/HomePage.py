from selenium.webdriver.common.by import By

from page_objects.DeleteAccount import DeleteAccount
from page_objects.LoginPage import LoginPage
from page_objects.Products import Products


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    category = (By.XPATH, "//h2[text()='Category']")
    login_btn = (By.XPATH, "//i[@class='fa fa-lock']")
    login_text = (By.XPATH, "//a[text()=' Logged in as ']/b")
    delete_btn = (By.XPATH, "//a[text()=' Delete Account']")
    products_btn = (By.XPATH, "//a[text()=' Products']")

    def verify_home_page(self):
        return self.driver.find_element(*HomePage.category)

    def click_login_btn(self):
        self.driver.find_element(*HomePage.login_btn).click()
        return LoginPage(self.driver)

    def validate_login_text(self):
        return self.driver.find_element(*HomePage.login_text).text

    def click_delete_btn(self):
        self.driver.find_element(*HomePage.delete_btn).click()
        return DeleteAccount(self.driver)

    def click_products_btn(self):
        self.driver.find_element(*HomePage.products_btn).click()
        return Products(self.driver)
