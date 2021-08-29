import unittest

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

from pages.main import MainPage
from pages.search import SearchPage


class SearchTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.main_page = MainPage(self.driver)
        self.search_page = SearchPage(self.driver)

    def test_search_test(self):
        self.main_page.search_item("test")
        self.search_page.check_if_alert_appears()

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
