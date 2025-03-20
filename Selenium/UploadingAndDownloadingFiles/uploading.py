
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = service)

# Open URL
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
myWait = WebDriverWait(driver,10)
upload = myWait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='singleFileInput']")))

upload.send_keys("C:/Users/91950/PythonProjects/Selenium/UploadingAndDownloadingFiles/file-sample_100kB.doc")

driver.find_element(By.XPATH,"//*[@id='singleFileForm']/button").click()
# Keep browser open
input("Press Enter to close the browser...")

# Close browser
driver.quit()

