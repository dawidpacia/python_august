from selenium import webdriver
import unittest

from webdriver_manager.chrome import ChromeDriverManager

from pages.account import AccountPage
from pages.login import LoginPage
from pages.main import MainPage


class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.main_page = MainPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.account_page = AccountPage(self.driver)

    def test_successful_login(self):
        self.main_page.navigate_to_login()
        self.login_page.login("seleniumremote@gmail.com", "test123")
        self.account_page.check_if_logged_in()

    def test_wrong_password(self):
        self.main_page.navigate_to_login()
        self.login_page.login("seleniumremote@gmail.com", "test1234")
        self.login_page.check_if_alert_appears()

    def test_no_password(self):
        self.main_page.navigate_to_login()
        self.login_page.login("seleniumremote@gmail.com", "")
        self.login_page.check_if_alert_appears()

    def test_wrong_email_format(self):
        self.main_page.navigate_to_login()
        self.login_page.login("seleniumremote", "test1234")
        self.login_page.check_if_alert_appears()


if __name__ == '__main__':
    unittest.main()
