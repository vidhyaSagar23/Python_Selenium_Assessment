import pytest
from selenium import webdriver

driver =None


@pytest.fixture(scope="class")
def setup(request):
    global driver
    driver = webdriver.Chrome()
    driver.get("https://automationexercise.com/")
    driver.maximize_window()
    driver.implicitly_wait(3)
    request.cls.driver = driver
    yield
    driver.close()
