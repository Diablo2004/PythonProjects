from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.action_chains import ActionChains

# Setup ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open URL
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()

min_slider = driver.find_element(By.XPATH,"//*[@id='slider-range']/span[1]")
max_slider = driver.find_element(By.XPATH,"//*[@id='slider-range']/span[2]")

print("Location of sliders before moving: ")
print(min_slider.location) # {'x': 59, 'y': 293}
print(max_slider.location) # {'x': 612, 'y': 293}

act = ActionChains(driver)

act.drag_and_drop_by_offset(min_slider,100,0).perform() # since we cant move in y direction
act.drag_and_drop_by_offset(max_slider, -40,0).perform()

print("Location of sliders after moving: ")
print(min_slider.location) # {'x': 159, 'y': 250}
print(max_slider.location) # {'x': 574, 'y': 250}

# Keep browser open
input("Press Enter to close the browser...")

# Close browser
driver.quit()
