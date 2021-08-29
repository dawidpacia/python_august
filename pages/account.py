from selenium.webdriver.common.by import By

from pages.base import BasePage


class AccountPage(BasePage):

    account_tab_selector = (By.CLASS_NAME, "account")


    def check_if_logged_in(self):
        self.driver.find_element(*self.account_tab_selector)