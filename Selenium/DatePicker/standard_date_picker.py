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
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.switch_to.frame(0)

# This should work 90% of the time:
# driver.find_element(By.XPATH,"//*[@id = 'datepicker']").send_keys("05/30/2022") # mm/dd/yyyy

# In case this doesnt:
year = "2025"
month = "June"
date = "15"

driver.find_element(By.XPATH,"//*[@id = 'datepicker']").click()
wait = WebDriverWait(driver, 10)

while True:
    try:
        mon = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='ui-datepicker-month']"))).text
        yr = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='ui-datepicker-year']"))).text

        if mon == month and yr == year:
            break
        else:
            driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[2]").click() # Next arrow
    except:
        print("Element went stale,retyring...")

# Select date
dates = driver.find_elements(By.XPATH,"//*[@id='ui-datepicker-div']//table/tbody/tr/td/a")

for ele in dates:
    if ele.text == date:
        ele.click()
        break

# Keep browser open
input("Press Enter to close the browser...")

# Close browser
driver.quit()
