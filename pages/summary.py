from selenium.webdriver.common.by import By

from pages.base import BasePage


class SummaryPage(BasePage):

    total_price_selector = (By.ID, "total_price_container")
    shipping_price_selector = (By.ID, "total_shipping")

    def check_total_price(self):
        element = self.driver.find_element(*self.total_price_selector)
        price = float(element.text[1:])
        return price

    def check_shipping_price(self):
        element = self.driver.find_element(*self.shipping_price_selector)
        price = float(element.text[1:])
        return price
