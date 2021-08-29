from selenium.webdriver.common.by import By

from pages.base import BasePage


class LoginPage(BasePage):

    email_field_selector = (By.ID, "email")
    password_field_selector = (By.ID, "passwd")
    submit_button_selector = (By.ID, "SubmitLogin")
    alert_box_selector = (By.CSS_SELECTOR, ".alert.alert-danger")

    def login(self, email, password):
        self.driver.find_element(*self.email_field_selector).send_keys(email)
        self.driver.find_element(*self.password_field_selector).send_keys(password)
        self.driver.find_element(*self.submit_button_selector).click()

    def check_if_alert_appears(self):
        self.driver.find_element(*self.alert_box_selector)
