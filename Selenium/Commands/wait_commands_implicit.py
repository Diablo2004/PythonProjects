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

driver.implicitly_wait(10) # seconds # implicit wait
# Applies to all elements globally.
# Waits for a fixed time before throwing NoSuchElementException.
# Once set, it remains active for the entire session.

# Open website
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")

driver.find_element(By.XPATH,"//button[contains(@class, 'orangehrm-login-button')]").click()

driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a").click()
# Keep browser open
input("Press Enter to close the browser...")

# Close browser
driver.quit()
