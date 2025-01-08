from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class BasePageElement(object):
    def __init__(self, locator):
        self.locator = locator

    def __set__(self, obj, value): # dunder method
        driver = obj.driver
        print(f"Waiting for element with name: {self.locator}")  # Debugging log
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(self.locator)
        )
        print(f"Element found. Setting value: {value}")  # Debugging log
        element = driver.find_element(*self.locator) # Unpacking tuple
        element.clear()
        element.send_keys(value)

    def __get__(self, obj, owner):
        driver = obj.driver
        print(f"Waiting for element with name: {self.locator}")  # Debugging log
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(self.locator)
        )
        element = driver.find_element(*self.locator)
        return element.get_attribute("value")