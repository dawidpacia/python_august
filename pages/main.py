from selenium.webdriver.common.by import By

from pages.base import BasePage


class MainPage(BasePage):

    search_field_selector = (By.ID, "search_query_top")
    search_button_selector = (By.XPATH, "//*[@name='submit_search']")
    login_button_selector = (By.CLASS_NAME, "login")

    def go_to_page(self, url):
        self.driver.get(url)

    def search_item(self):
        self.driver.find_element(*self.search_field_selector).send_keys("test")
        self.driver.find_element(*self.search_button_selector).click()

    def navigate_to_login(self):
        self.driver.find_element(*self.login_button_selector).click()
