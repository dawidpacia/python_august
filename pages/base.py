from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class BasePage:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.driver.get("http://automationpractice.com/index.php")

























class WebDriver:

    class __WebDriver:
        def __init__(self):
            self.driver = webdriver.Chrome(ChromeDriverManager().install())

    driver = None

    def __init__(self):
        if not self.driver:
            WebDriver.driver = WebDriver.__WebDriver().driver
