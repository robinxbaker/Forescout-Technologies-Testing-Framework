# Web scraper and tester for yahoo finance
# Tests whether certain index funds have risen or fallen

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = "C:/Program Files/chromedriver-win64/chromedriver.exe"

service = Service(PATH)

driver = webdriver.Chrome(service=service)

driver.get("https://finance.yahoo.com/")


try:
    # Open the yahoo finance page
    driver.get("https://finance.yahoo.com/")
    driver.maximize_window()

    stocks = ["S&P", "DOW", "NASDAQ", "CRUDE", "GOLD", "SILVER"]
    price_change = [None * len(stocks)]

    for i, stock in enumerate(stocks):


        # <input type="text" class="_yb_1tvko3e _yb_1da8usa _yb_18ya2pl finsrch-inpt rounded" id="ybar-sbq" name="p" value="" autocomplete="off" data-ylk="sec:ybar;slk:websrch;subsec:searchbox;elm:search;elmt:input;itc:0;" placeholder="Search for news, symbols or companies" aria-activedescendant="" data-rapid_p="279" data-v9y="1">

        # Wait for the search icon to be present
        search_bar = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.ID, "ybar-sbq")
            )
        )

        # Simulate moving the mouse over the search icon and clicking it
        actions = ActionChains(driver)
        actions.move_to_element(search_bar).pause(1).click().perform()  # Add a 1-second pause before clicking
        actions.send_keys(stock).perform()
        actions.pause(3).send_keys(Keys.RETURN).pause(2).perform()

        neg_or_pos = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "fin-streamer.priceChange")
            )
        )

        price_change = neg_or_pos.get_attribute("data-value")

        if int(price_change) > 0:
            price_change[i] = "+"

        print(price_change)

        time.sleep(2)

    # Implement unittesting here ###############################################


finally:
    # Close the browser
    driver.quit()