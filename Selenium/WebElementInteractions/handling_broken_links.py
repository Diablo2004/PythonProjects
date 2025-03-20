import requests as requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open URL
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()
driver.implicitly_wait(10)

all_links = driver.find_elements(By.TAG_NAME,"a")
count = 0

for link in all_links:
    url = link.get_attribute('href')
    try:
        res = requests.head(url)
    except:
        None
    if res.status_code >= 400:
        print(url," is a broken link")
        count+=1
    else:
        print(url," is a valid link")

print("Total number of broken links: ",count)

# Keep browser open
input("Press Enter to close the browser...")

# Close browser
driver.quit()

