from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.action_chains import ActionChains

# Setup ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open URL
driver.get("https://api.jquery.com/dblclick/")

# Switch to iframe
driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))

# Locate the element to double-click
box = driver.find_element(By.TAG_NAME, "div")

# Perform double click
actions = ActionChains(driver)
time.sleep(5)
actions.double_click(box).perform()

# Keep browser open
input("Press Enter to close the browser...")

# Close browser
driver.quit()
