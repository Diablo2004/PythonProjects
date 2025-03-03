from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open URL
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# Handling a simple alert
driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
alert = driver.switch_to.alert
print(alert.text)
time.sleep(5)
alert.accept()

# Handling a confirmation alert (OK/Cancel)
driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
alert = Alert(driver)
time.sleep(5)
alert.dismiss()  # Clicks 'Cancel'

# Handling a prompt alert (Input required)
driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
alert = Alert(driver)
alert.send_keys("Selenium Test")
alert.accept()

time.sleep(3)
driver.quit()
