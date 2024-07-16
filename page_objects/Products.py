import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.ViewCart import ViewCart


class Products:
    def __init__(self, driver):
        self.driver = driver

    product1 = (By.CSS_SELECTOR, "img[src='/get_product_picture/1']")
    first_card = (By.XPATH, "(//div[@class='col-sm-9 padding-right']//div[2]//div[1]//div[1]//div[2]//div[1]//a[1])")

    product2 = (By.CSS_SELECTOR, "img[src='/get_product_picture/2']")
    second_card = (By.XPATH, "//body/section/div[@class='container']/div[@class='row']/div[@class='col-sm-9 "
                             "padding-right']/div[@class='features_items']/div[3]/div[1]/div[1]/div[2]/div[1]/a[1]")

    continue_btn = (By.XPATH, "//button[text()='Continue Shopping']")
    view_cart = (By.XPATH, "//u[text()='View Cart']")

    def select_first_product(self):
        product_card = self.driver.find_element(*Products.product1)
        action = ActionChains(self.driver)
        action.move_to_element(product_card).perform()
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "(//div[@class='col-sm-9 "
                                                                                "padding-right']//div[2]//div["
                                                                                "1]//div[1]//div[2]//div[1]//a[1])")))
        self.driver.find_element(*Products.first_card).click()

    def select_second_product(self):
        product_card = self.driver.find_element(*Products.product2)
        action = ActionChains(self.driver)
        action.move_to_element(product_card).perform()
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//body/section/div["
                                                                                "@class='container']/div["
                                                                                "@class='row']/div[@class='col-sm-9 "
                                                                                "padding-right']/div["
                                                                                "@class='features_items']/div[3]/div["
                                                                                "1]/div[1]/div[2]/div[1]/a[1]")))
        self.driver.find_element(*Products.second_card).click()

    def click_continue(self):
        self.driver.find_element(*Products.continue_btn).click()

    def click_view_cart(self):
        self.driver.find_element(*Products.view_cart).click()
        return ViewCart(self.driver)
