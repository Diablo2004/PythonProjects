from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://opensource-demo.orangehrmlive.com/") # opening the browser with get
driver.maximize_window() # maximize the browser window

print(driver.title) # to capture the title of the current webpage
print(driver.current_url) # to capture and verify the current url of the webpage
print(driver.page_source) # to capture the source code

# Keep browser open
input("Press Enter to close the browser...")

# Close browser
driver.quit()
