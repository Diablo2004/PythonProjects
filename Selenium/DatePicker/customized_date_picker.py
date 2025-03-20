
from selenium.webdriver.support.select import Select
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
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

# Date of Birth

driver.find_element(By.XPATH,"//input[@id = 'dob']").click()

month = Select(driver.find_element(By.XPATH,"//*[@id = 'ui-datepicker-div']/div[1]/div/select[1]"))
month.select_by_visible_text("Apr")

year = Select(driver.find_element(By.XPATH,"//*[@id = 'ui-datepicker-div']/div[1]/div/select[2]"))
year.select_by_visible_text("2004")

dates = driver.find_elements(By.XPATH,"//div[@id = 'ui-datepicker-div']//table/tbody/tr/td/a")

for date in dates:
    if date.text == "29":
        date.click()
        break

#Keep browser open
input("Press Enter to close the browser...")

# Close browser
driver.quit()
