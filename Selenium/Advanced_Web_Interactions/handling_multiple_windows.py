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
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
driver.implicitly_wait(10)

# every window has its specific id, changes at every instance
# windowId = driver.current_window_handle
# print("Current window ID: ",windowId)

# opening new window
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()

# capturing all window ids
windowIDs = driver.window_handles

parent_window = windowIDs[0]
child_window = windowIDs[1]

# print(parent_window,child_window)

# Switching windows
# Approach 1 for less windows

# driver.switch_to.window(child_window)
# print("Title of the child window: ",driver.title)
#
# driver.switch_to.window(parent_window)
# print("Title of the parent window ",driver.title)

# Approach 2 for more windows

# for winid in windowIDs:
#     driver.switch_to.window(winid)
#     print(driver.title)

# Closing specific windows

for winid in windowIDs:
    driver.switch_to.window(winid)
    time.sleep(3)
    if driver.title == "OrangeHRM":
        driver.close()

# Keep browser open
input("Press Enter to close the browser...")

# Close browser
driver.quit()

