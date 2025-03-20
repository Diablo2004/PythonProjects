from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://demo.nopcommerce.com/") # opening the browser with get
driver.maximize_window() # maximize the browser window

# find_element() - Returns single web element

# 1) Locator matching with single element
# element = driver.find_element(By.XPATH,"//input[@id = 'small-searchterms']")
# element.send_keys("Apple MacBook Pro 13 inch")

# 2) Locator matching with multiple web elements
# element = driver.find_element(By.XPATH,"//div[@class = 'footer']//a")
# print(element.text) # prints first link from the footer - "Sitemap"

# 3) Element not available throws NoSuchElementException
# login_element = driver.find_element(By.LINK_TEXT,"Log")
# login_element.click()

# find_elements() - Returns multiple web elements

# 1) Locator matching with single element
elements = driver.find_elements(By.XPATH,"//input[@id = 'small-searchterms']")
print(len(elements)) # 1
elements[0].send_keys("Apple MacBook Pro 13 inch")

# 2) Locator matching with multiple elements
elements = driver.find_elements(By.XPATH,"//div[@class = 'footer']//a")
print(len(elements)) # 24
# print(elements[0].text) # Sitemap
for ele in elements:
    print(ele.text)

# 3) Elements not available - 0
elements = driver.find_elements(By.LINK_TEXT,"Log")
print("elements returned: ",len(elements))

# Keep browser open
input("Press Enter to close the browser...")

# Close browser
driver.quit()
