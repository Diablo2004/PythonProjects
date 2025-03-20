from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.facebook.com/") # opening the browser with get
driver.maximize_window() # maximize the browser window

wait = WebDriverWait(driver, 20)

# Create new account
driver.find_element(By.XPATH,"//a[contains(@data-testid, 'registration')]").click()

# First Name
driver.find_element(By.XPATH,"//input[contains(@name,'firstname')]").send_keys("Mehul")

# Surname
driver.find_element(By.XPATH,"//input[contains(@name,'lastname')]").send_keys("Gupta")

# Birth-Date
day = Select(driver.find_element(By.XPATH,"//select[contains(@id,'day')]"))
for opt in day.options:
    print(opt.text)

day.select_by_visible_text('29')

month = Select(driver.find_element(By.XPATH,"//select[contains(@id,'month')]"))
for opt in month.options:
    print(opt.text)

month.select_by_index(3)

year = Select(driver.find_element(By.XPATH,"//select[contains(@id,'year')]"))
for opt in year.options:
    print(opt.text)

year.select_by_value('2004')

# Sex
driver.find_element(By.XPATH,"//input[starts-with(@id,'sex') and @value = '2']").click()

# Mobile number or email address
driver.find_element(By.XPATH,"//input[starts-with(@class,'inputtext') and contains(@aria-label,'Mobile number')]").send_keys("9509705221")

# New Password
driver.find_element(By.XPATH,"//input[starts-with(@name,'reg_passwd')]").send_keys("Naruto2004")

# Sign Up
driver.find_element(By.XPATH,"//button[text() = 'Sign Up' and @name = 'websubmit']").click()

# Find Account
element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Yes, Find My Account")))
element.click()

# Keep browser open
input("Press Enter to close the browser...")

# Close browser
driver.quit()
