from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.driver.get("http://automationpractice.com/index.php")

    def mouse_hover(self, selector):
        element = self.driver.find_element(*selector)
        ActionChains(self.driver).move_to_element(element).perform()

    def wait_for_clickable_element(self, selector):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(selector))





















class WebDriver:

    class __WebDriver:
        def __init__(self):
            self.driver = webdriver.Chrome(ChromeDriverManager().install())

    driver = None

    def __init__(self):
        if not self.driver:
            WebDriver.driver = WebDriver.__WebDriver().driver
