from selenium.webdriver.common.by import By

from pages.base import BasePage


class SearchPage(BasePage):

    no_result_box_selector = (By.CSS_SELECTOR, ".alert.alert-warning")
    product_container_selector = (By.CLASS_NAME, "product-container")
    add_to_cart_button_selector = (By.XPATH, "//*[@title='Add to cart']")
    proceed_to_checkout_button_selector = (By.XPATH, "//*[@title='Proceed to checkout']")
    continue_shopping_selector = (By.XPATH, "//*[@title='Continue shopping']")

    def check_if_alert_appears(self):
        self.driver.find_element(*self.no_result_box_selector)

    def add_to_basket(self):
        self.mouse_hover(self.product_container_selector)
        self.driver.find_element(*self.add_to_cart_button_selector).click()

    def proceed_to_checkout(self):
        self.wait_for_clickable_element(self.proceed_to_checkout_button_selector)
        self.driver.find_element(*self.proceed_to_checkout_button_selector).click()

    def continue_shopping(self):
        self.wait_for_clickable_element(self.continue_shopping_selector)
        self.driver.find_element(*self.continue_shopping_selector).click()