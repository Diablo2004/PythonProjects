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

# Open website
driver.get("https://www.snapdeal.com/")

driver.get("https://www.amazon.in/")

driver.back() # snapdeal
time.sleep(5)
driver.forward() # amazon
time.sleep(5)
driver.refresh() # refresh


# Keep browser open
input("Press Enter to close the browser...")

# Close browser
driver.quit()
