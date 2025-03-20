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
driver.get("http://testautomationpractice.blogspot.com/")
driver.maximize_window()

# 1) Count number of rows and columns

rows = len(driver.find_elements(By.XPATH,"//table[@name = 'BookTable']//tr"))
columns = len(driver.find_elements(By.XPATH,"//table[@name = 'BookTable']//tr[1]/th"))

print(rows) # 7
print(columns) # 4

# 2) Read specific row and column data

data = driver.find_element(By.XPATH,"//table[@name = 'BookTable']/tbody/tr[5]/td[1]").text
# print(data) # Master in Selenium

# 3) Read all the rows and columns data

print("printing all the rows and columns data..")

for r in range(2, rows + 1):
    for c in range(1, columns + 1):
        data = driver.find_element(By.XPATH,f"//table[@name = 'BookTable']/tbody/tr[{r}]/td[{c}]").text
        print(data,end = "            ")
    print()

# 4) Read data based on condition (List books name whose author is Mukesh)

for r in range(2,rows + 1):
    author = driver.find_element(By.XPATH,f"//table[@name = 'BookTable']/tbody/tr[{r}]/td[2]").text
    if author == 'Mukesh':
        bookName = driver.find_element(By.XPATH,f"//table[@name = 'BookTable']/tbody/tr[{r}]/td[1]").text
        print(bookName,"        ",author)


# Keep browser open
input("Press Enter to close the browser...")

# Close browser
driver.quit()

