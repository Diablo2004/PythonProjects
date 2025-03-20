from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

myWait = WebDriverWait(driver,10) # explicit wait declaration
# Waits until a specific condition is met.
# More flexible than Implicit Wait.
# Uses WebDriverWait + expected_conditions.

# myWait = WebDriverWait(driver,10, poll_frequency = 2, ignored_exceptions =[NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException,Exception]) # fluent wait declaration
# Similar to Explicit Wait but with polling intervals.
# Retries every few seconds instead of waiting the full time.
# Can ignore exceptions like NoSuchElementException.

# Open website
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

myWait.until(EC.presence_of_element_located((By.NAME,"username"))).send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
myWait.until(EC.element_to_be_clickable((By.XPATH,"//button[contains(@class, 'orangehrm-login-button')]"))).click()

myWait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a"))).click()
# Keep browser open
input("Press Enter to close the browser...")

# Close browser
driver.quit()
