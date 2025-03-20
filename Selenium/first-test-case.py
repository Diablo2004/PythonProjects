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
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.implicitly_wait(10)  # Implicit wait for elements to load

# Locate elements and send keys
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")

# Wait until the login button is clickable
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'orangehrm-login-button')]"))
)
login_button.click()



# Wait for the page to load after login
time.sleep(2)  # Use WebDriverWait if checking for a specific element

# Validate login
act_title = driver.title
exp_title = "OrangeHRM"

if act_title == exp_title:
    print("Login test passed")
else:
    print("Login Test failed")

# Keep browser open
input("Press Enter to close the browser...")

# Close browser
driver.quit()
