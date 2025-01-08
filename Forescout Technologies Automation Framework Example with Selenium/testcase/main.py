import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import page
import time

PATH = "C:/Program Files/chromedriver-win64/chromedriver.exe"
SEARCH_TERMS = {
    "stocks": ["DOW", "NASDAQ", "S&P"],
    "metals": ["GOLD", "SILVER", "PLATINUM"]
}

SEARCH_TERMSS = ["DOW", "NASDAQ", "S&P", "GOLD", "SILVER", "CRUDE"]

class YahooFinanceTests(unittest.TestCase):

    def setUp(self):
        service = Service(PATH)
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://finance.yahoo.com/")
        self.driver.maximize_window()
        time.sleep(5)

    def test_price_change(self):
        """
        Test daily price change for multiple search terms.
        """
        finance_page = page.YahooFinancePage(self.driver)

        for term in SEARCH_TERMSS:
            with self.subTest(term=term):
                finance_page.search(term)
                price_change = finance_page.get_daily_price_change()

                # Parse price change string

                is_positive = price_change > 0
                print(f"{term}: {'Positive' if is_positive else 'Negative'} ({price_change})")
                self.assertTrue(is_positive)

    def test_stocks_vs_metals(self):
        """
        Test whether stocks are outmatching materials in terms of daily price change.
        """
        finance_page = page.YahooFinancePage(self.driver)

        stocks_changes = []
        metals_changes = []

        for group, terms in SEARCH_TERMS.items():
            for term in terms:
                with self.subTest(term=term):
                    finance_page.search(term)
                    price_change = finance_page.get_daily_price_change()

                    print(f"{term}: {price_change}")
                    
                    # Add price change to the respective group
                    if group == "stocks":
                        stocks_changes.append(price_change)
                    elif group == "metals":
                        metals_changes.append(price_change)

        # Calculate the total or average price change for each group
        stocks_total = sum(stocks_changes)
        metals_total = sum(metals_changes)

        print(f"Stocks Total Change: {stocks_total}")
        print(f"Metals Total Change: {metals_total}")

        # Assert that stocks are outperforming materials
        self.assertGreater(
            stocks_total, metals_total,
            "Stocks are not outmatching metals in daily price changes"
        )


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()