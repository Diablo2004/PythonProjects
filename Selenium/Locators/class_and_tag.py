from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.inmotionhosting.com/") # opening the browser with get
driver.maximize_window() # maximize the browser window

# To find more than one element - class-name and tag-name

sliders = driver.find_elements(By.CLASS_NAME,"imh-rostrum-card")
print(len(sliders))

links = driver.find_elements(By.TAG_NAME,"a")
print(len(links))

# Keep browser open
input("Press Enter to close the browser...")

# Close browser
driver.quit()