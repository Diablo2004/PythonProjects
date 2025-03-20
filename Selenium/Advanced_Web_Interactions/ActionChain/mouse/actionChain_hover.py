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
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(10)

# Find the element to hover over
menu = driver.find_element(By.XPATH, "//*[@id='HTML3']/div[1]/div/button")

# Create an ActionChains object
actions = ActionChains(driver)

# Hover over the menu
actions.move_to_element(menu).perform()

# Pause to see the effect
time.sleep(10)

# Click on "Mobile" after hovering
driver.find_element(By.XPATH, "//*[@id='HTML3']/div[1]/div/div/a[1]").click()


# Keep browser open
input("Press Enter to close the browser...")

# Close browser
driver.quit()
