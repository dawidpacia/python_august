import unittest

from hamcrest import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

from pages.main import MainPage
from pages.search import SearchPage
from pages.summary import SummaryPage


class TestBasket(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.main_page = MainPage(self.driver)
        self.search_page = SearchPage(self.driver)
        self.summary_page = SummaryPage(self.driver)

    def test_add_printed_summer(self):
        self.main_page.search_item("Printed Summer")
        self.search_page.add_to_basket()
        self.search_page.proceed_to_checkout()
        total_price = self.summary_page.check_total_price()
        assert_that(total_price, greater_than_or_equal_to(20))
        shipping_price = self.summary_page.check_shipping_price()
        assert_that(shipping_price, equal_to(2))

    def test_add_blouse_and_dress(self):
        self.main_page.search_item("Blouse")
        self.search_page.add_to_basket()
        self.search_page.continue_shopping()

        self.main_page.search_item("Dress")
        self.search_page.add_to_basket()
        self.search_page.proceed_to_checkout()

        total_price = self.summary_page.check_total_price()
        assert_that(total_price, greater_than_or_equal_to(20))
        shipping_price = self.summary_page.check_shipping_price()
        assert_that(shipping_price, equal_to(2))

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
