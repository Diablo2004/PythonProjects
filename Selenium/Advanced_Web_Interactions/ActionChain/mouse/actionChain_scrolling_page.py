from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open URL
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()

# Explicit Wait for page to load completely
wait = WebDriverWait(driver, 20)
wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='section-nav']/ul/li[1]/a")))

# 1. Scroll down page by pixel
# driver.execute_script("window.scrollBy(0,3000)","")
# values = driver.execute_script("return window.pageYOffset")
# print("Number of pixels moved: ",values)

# 2. Scroll down page till the element is visible
# flag = driver.find_element(By.XPATH,"//img[@alt = 'Flag of India']")
# driver.execute_script("arguments[0].scrollIntoView();",flag)
# driver.execute_script(...) → Executes JavaScript in the browser.
# arguments[0] → Refers to the first argument passed (flag in this case).
# .scrollIntoView(); → A JavaScript function that scrolls the page until the element is in view.
# values = driver.execute_script("return window.pageYOffset")
# print("Number of pixels moved: ",values)

# 3. Scroll down page till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
values = driver.execute_script("return window.pageYOffset")
print("Number of pixels moved: ",values)

time.sleep(5)

# Scroll up to starting position
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
values = driver.execute_script("return window.pageYOffset")
print("Number of pixels moved: ",values)

# Keep browser open
input("Press Enter to close the browser...")

# Close browser
driver.quit()
