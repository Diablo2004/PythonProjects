import requests as requests
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Ctrl + A
# Ctrl + C
# Tab
# Ctrl + V

# Setup ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open URL
driver.get("https://text-compare.com/")
driver.maximize_window()

input1 = driver.find_element(By.XPATH,"//*[@id='inputText1']")
input2 = driver.find_element(By.XPATH,"//*[@id='inputText2']")

input1.send_keys("welcome to selenium")

act = ActionChains(driver)

# input1 ---> Ctrl + A
act.key_down(Keys.CONTROL)
act.send_keys("a")
act.key_up(Keys.CONTROL)
act.perform()

# act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

# input1 ---> Ctrl + C
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

# Press Tab key to navigate to input2

act.send_keys(Keys.TAB).perform()

# input2 ---> Ctrl + V
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

# Keep browser open
input("Press Enter to close the browser...")

# Close browser
driver.quit()

