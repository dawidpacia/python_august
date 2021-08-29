from selenium.webdriver.common.by import By

from pages.base import BasePage


class SearchPage(BasePage):

    no_result_box_selector = (By.CSS_SELECTOR, ".alert.alert-warning")

    def check_if_alert_appears(self):
        self.driver.find_element(*self.no_result_box_selector)
