import os

import requests as requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

location = os.getcwd()

# Setup ChromeDriver
service = Service(ChromeDriverManager().install())
# Downloading files in desired location
preferences = {"download.default_directory": location,"plugins.always_open_pdf_externally":True}
ops = webdriver.ChromeOptions()
ops.add_experimental_option("prefs",preferences)
driver = webdriver.Chrome(service = service,options = ops)

myWait = WebDriverWait(driver,10)

# Open URL
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
driver.maximize_window()


myWait.until(EC.element_to_be_clickable((By.XPATH,"//tbody/tr[1]/td[5]/a[1]"))).click()


# Keep browser open
input("Press Enter to close the browser...")

# Close browser
driver.quit()

