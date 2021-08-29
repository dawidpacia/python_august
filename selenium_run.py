from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("--start-maximized")


driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_option)

driver.get("http://automationpractice.com/index.php")


# selectors
driver.find_element_by_id("header_logo")
driver.find_element_by_class_name("shopping_cart")
driver.find_element_by_id("newsletter-input")
driver.find_element_by_class_name("twitter")
driver.find_element_by_class_name("homefeatured")
driver.find_element_by_id("contact-link")

# css selectors
driver.find_element_by_css_selector(".logo")
driver.find_element_by_css_selector(".shopping_cart > a")
driver.find_element_by_css_selector("#newsletter-input[name='email']")
driver.find_element_by_css_selector(".twitter > a")
driver.find_element_by_css_selector(".homefeatured[data-toggle='tab']")
driver.find_element_by_css_selector("a[title='Contact Us']")

# xpath selectors
driver.find_element_by_xpath("//div[@id='header_logo']//img")
driver.find_element_by_xpath("//*[@class='shopping_cart']/a")
driver.find_element_by_xpath("//input[@id='newsletter-input']")
driver.find_element_by_xpath("//*[@class='twitter']/a")
driver.find_element_by_xpath("//*[@class='homefeatured']")
driver.find_element_by_xpath("//*[@title='Contact Us']")


driver.find_element_by_id("newsletter-input").send_keys("test")

# logo = driver.find_element_by_id("header_logo")
# logo.click()


# driver.quit()