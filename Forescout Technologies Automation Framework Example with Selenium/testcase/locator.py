from selenium.webdriver.common.by import By

class YahooFinanceLocators(object):
    SEARCH_BAR = (By.ID, "ybar-sbq")
    DAILY_PRICE_CHANGE = (By.CSS_SELECTOR, "fin-streamer.priceChange.yf-1tejb6")