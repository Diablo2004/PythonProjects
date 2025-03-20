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
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

# Locate the button to right-click
button = driver.find_element(By.CLASS_NAME, "context-menu-one")

# Perform right-click
actions = ActionChains(driver)
actions.context_click(button).perform()

# Click an option from the right-click menu
driver.find_element(By.XPATH, "//li[contains(@class,'edit')]").click()

alert = driver.switch_to.alert
print(alert.text)

alert.accept()
# Keep browser open
input("Press Enter to close the browser...")

# Close browser
driver.quit()
