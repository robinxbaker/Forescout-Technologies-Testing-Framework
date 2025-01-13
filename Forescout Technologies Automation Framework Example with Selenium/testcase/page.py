from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locator import YahooFinanceLocators
from element import BasePageElement
import time

# Inheriting from object ensures that BasePage is a new-style class. All classes in python 3 are new-style, but this ensures that code is compatible with python 2.
class BasePage(object):
    """Base class for all page objects"""

    def __init__(self, driver):
        """Initializes page with driver object.
        When other classes inherit BasePage, they will have driver"""
        self.driver = driver

class YahooFinancePage(BasePage):
    search_bar = BasePageElement(YahooFinanceLocators.SEARCH_BAR)

    def is_title_matches(self):
        return "Yahoo Finance" in self.driver.title
    
    def search(self, text):
        """
        Type text into the search bar and submit.
        """
        # Use the `search_bar` descriptor to set the text
        self.search_bar = text  # This triggers the `__set__` method in BasePageElement
        
        # Submit the search (this uses the already located element)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(YahooFinanceLocators.SEARCH_BAR)
        ).send_keys(Keys.ENTER)

        # Wait for the results to load
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(YahooFinanceLocators.DAILY_PRICE_CHANGE)
        )
        time.sleep(5)


    def get_daily_price_change(self):
        """
        Retrieve the daily price change from the search results
        """

        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(YahooFinanceLocators.DAILY_PRICE_CHANGE)
        )
        data_value = element.get_attribute("data-value")
        return float(data_value)
