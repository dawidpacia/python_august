import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from hamcrest import *


class TestClass(unittest.TestCase):

    def setUp(self):
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_option)
        self.driver.get("http://automationpractice.com/")

    def test_addresses(self):
        self.driver.find_element_by_class_name("login").click()
        self.driver.find_element_by_id("email").send_keys("seleniumremote@gmail.com")
        self.driver.find_element_by_id("passwd").send_keys("test123")
        self.driver.find_element_by_id("SubmitLogin").click()
        self.driver.find_element_by_xpath("//*[@title='Addresses']").click()
        addresses = self.driver.find_elements_by_css_selector(".bloc_adresses.row > div")

        assert_that(addresses, is_not(empty()))

    @unittest.skip
    def test_credit_slips(self):
        pass


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

