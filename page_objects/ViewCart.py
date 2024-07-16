from selenium.webdriver.common.by import By

from test_data.TestData import TestData


class ViewCart:
    def __init__(self, driver):
        self.driver = driver
        self.data = TestData()

    products_element = (By.XPATH, "//td[@class='cart_description']/h4/a")
    blue_cloth_quantity = (By.XPATH, "(//td[@class='cart_quantity']/button)[1]")
    men_cloth_quantity = (By.XPATH, "(//td[@class='cart_quantity']/button)[2]")

    blue_cloth_total = (By.XPATH, "(//p[@class='cart_total_price'])[1]")
    men_cloth_total = (By.XPATH, "(//p[@class='cart_total_price'])[2]")

    def checkProductIsVisible(self):
        products = self.driver.find_elements(*ViewCart.products_element)
        for product in products:
            assert self.data.cloth1 in product.text or self.data.cloth2 in product.text

    def verify_quantity(self):
        assert self.driver.find_element(*ViewCart.blue_cloth_quantity).text == self.data.quantity
        assert self.driver.find_element(*ViewCart.men_cloth_quantity).text == self.data.quantity

    def verify_total(self):
        assert self.data.price1 in self.driver.find_element(*ViewCart.blue_cloth_total).text
        assert self.data.price2 in self.driver.find_element(*ViewCart.men_cloth_total).text





