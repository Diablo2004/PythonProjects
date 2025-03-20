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
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()

source = driver.find_element(By.ID,"box6")
target = driver.find_element(By.ID,"box106")

act = ActionChains(driver)
act.drag_and_drop(source,target).perform()

# Keep browser open
input("Press Enter to close the browser...")

# Close browser
driver.quit()
