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
driver.get("https://ui.vision/demo/webtest/frames/")
driver.maximize_window()
driver.implicitly_wait(10)

# switch to frame using
# 1) switch_to.frame(name of the frame)
# 2) switch_to.frame(id of the frame)
# 3) switch_to.frame(web element)
# 4) switch_to.frame(index)

# switching to frame 1
frame = driver.find_element(By.XPATH,"//frame[contains(@src, 'frame_1.html')]")
driver.switch_to.frame(frame)

driver.find_element(By.XPATH,"//input[@name = 'mytext1']").send_keys("input example")

#switching to main frame
driver.switch_to.default_content()

# switching to frame 2
frame = driver.find_element(By.XPATH,"//frame[starts-with(@src, 'frame_2')]")
driver.switch_to.frame(frame)

driver.find_element(By.XPATH,"//input[@name = 'mytext2']").send_keys("input example 2")

#switching to main frame
driver.switch_to.default_content()

# Inline frames
# An iFrame (inline frame) is an HTML element that allows embedding another document within the current page.
# We need to switch to the iFrame before interacting with elements inside it.

# switching to outer frame
outer_frame = driver.find_element(By.XPATH,"//frame[@src = 'frame_3.html']")
driver.switch_to.frame(outer_frame)

driver.find_element(By.XPATH,"//input[@name='mytext3']").send_keys("input example 3")

# switching to inner frame
inner_frame = driver.find_element(By.XPATH,"//iframe[contains(@width, '650') and contains(@height, '350')]")
driver.switch_to.frame(inner_frame)

driver.find_element(By.XPATH,"//div[@id= 'i9']").click()

# switching back to parent frame
driver.switch_to.parent_frame()

parent_frame = (driver.find_element(By.XPATH,"//input[@name='mytext3']"))
time.sleep(5)
parent_frame.clear()
time.sleep(5)
parent_frame.send_keys("back to parent frame")

# Keep browser open
input("Press Enter to close the browser...")

# Close browser
driver.quit()

