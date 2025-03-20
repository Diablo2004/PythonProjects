from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open URL
driver.get("https://www.qa-practice.com/elements/checkbox/mult_checkbox")
driver.maximize_window()

# 1) Select specific checkbox
# driver.find_element(By.XPATH,"//input[@id = 'id_checkboxes_0']").click()

# 2) Select all the checkboxes
checkboxes = driver.find_elements(By.XPATH, "//input[@type = 'checkbox' and contains(@name, 'checkboxes')]")
print(len(checkboxes)) # 3

# selecting all
# for checkbox in checkboxes:
#     checkbox.click()

# 3) Select multiple checkboxes by choice
for checkbox in checkboxes:
    name = checkbox.get_attribute('value')
    print(name)
    if name == 'two' or name == 'three':
        checkbox.click()

time.sleep(5)

# 4) Clearing all the checkboxes
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()

# Keep browser open
input("Press Enter to close the browser...")

# Close browser
driver.quit()
