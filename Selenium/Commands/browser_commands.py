from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open URL
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

# Wait until the element is present
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "OrangeHRM, Inc")))

# Click the element
element.click()

input("Press enter to close the browser...")
# Close window
# driver.close()

# Close browser
driver.quit()
