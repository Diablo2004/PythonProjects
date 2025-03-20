import requests as requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open URL
driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()

wait = WebDriverWait(driver,10)

# Login
wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"))).send_keys("Admin")
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123")
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()

# Admin --> user management --> users
wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a"))).click()
wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span/i"))).click()
wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li/a"))).click()

# total rows in a table
rows = len(driver.find_elements(By.XPATH,f"//table[@id = 'resultTable']/tbody/tr"))
print("Total number of rows in a table: ",rows)

count = 0
for r in range(1,rows+1):
    status = driver.find_element(By.XPATH,f"//table[@id = 'resultTable']/tbody/tr[{r}]/td[5]").text
    if status == "Enabled":
        count += 1

print("Total number of users: ",rows)
print("Number of users enabled: ",count)
print("Number of disabled users: ",(rows-count))

# Keep browser open
input("Press Enter to close the browser...")

# Close browser
driver.quit()

