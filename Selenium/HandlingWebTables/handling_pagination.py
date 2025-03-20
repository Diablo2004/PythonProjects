from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open the website
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(2)  # Allow page to load

# Find total number of pages
pages = driver.find_elements(By.XPATH, "//ul[@id='pagination']/li/a")
total_pages = len(pages)

for page in range(1, total_pages + 1):
    print(f"\nScraping Page {page}...\n")

    # Extract all rows from the table
    rows = driver.find_elements(By.XPATH, "//table[@id='productTable']//tbody/tr")

    for row in rows:
        columns = row.find_elements(By.TAG_NAME, "td")
        data = [col.text for col in columns]
        print(data)

    # Click on the next page number
    if page < total_pages:
        next_page = driver.find_element(By.XPATH, f"//ul[@id='pagination']/li/a[text()='{page + 1}']")
        driver.execute_script("arguments[0].click();", next_page)
        time.sleep(2)

# Close browser
driver.quit()
