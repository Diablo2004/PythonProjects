import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open URL
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# Providing complete path
# driver.save_screenshot("C:/Users/91950/PythonProjects/Selenium/HandlingScreenshots/homepage.png")

# Provide current working directory
# driver.save_screenshot(os.getcwd() + "/homepage.png")

# Save as a file
driver.get_screenshot_as_file(os.getcwd()+ "/homepage.png")

# two more methods: save as png and save as base64 - not generally used

# Keep browser open
input("Press Enter to close the browser...")

# Close browser
driver.quit()
