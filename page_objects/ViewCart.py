from selenium.webdriver.common.by import By


class ViewCart:
    def __init__(self, driver):
        self.driver = driver

    products_element = (By.XPATH, "//td[@class='cart_description']/h4/a")
    blue_cloth_quantity = (By.XPATH, "(//td[@class='cart_quantity']/button)[1]")
    men_cloth_quantity = (By.XPATH, "(//td[@class='cart_quantity']/button)[2]")

    blue_cloth_total = (By.XPATH, "(//p[@class='cart_total_price'])[1]")
    men_cloth_total = (By.XPATH, "(//p[@class='cart_total_price'])[2]")

    def checkProductIsVisible(self):
        products = self.driver.find_elements(*ViewCart.products_element)
        for product in products:
            print(product.text)
            assert "Blue Top" in product.text or "Men Tshirt" in product.text

    def verify_quantity(self):
        assert self.driver.find_element(*ViewCart.blue_cloth_quantity).text == "1"
        assert self.driver.find_element(*ViewCart.men_cloth_quantity).text == "1"

    def verify_total(self):
        # print(self.driver.find_element(*ViewCart.blue_cloth_total).text)
        assert "500" in self.driver.find_element(*ViewCart.blue_cloth_total).text
        assert "400" in self.driver.find_element(*ViewCart.men_cloth_total).text





