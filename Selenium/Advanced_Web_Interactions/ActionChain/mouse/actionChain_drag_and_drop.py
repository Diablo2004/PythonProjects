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
driver.get("https://jqueryui.com/droppable/")

# Switch to iframe (jQuery UI example uses an iframe)
driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))

# Locate the source and target elements
source = driver.find_element(By.ID, "draggable")
target = driver.find_element(By.ID, "droppable")

# Perform drag and drop
actions = ActionChains(driver)
actions.drag_and_drop(source, target).perform()

# Pause to see result
time.sleep(2)

# Keep browser open
input("Press Enter to close the browser...")

# Close browser
driver.quit()
