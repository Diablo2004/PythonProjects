from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://demo.nopcommerce.com/register") # opening the browser with get
driver.maximize_window() # maximize the browser window

# is_displayed - checks if the element is visible on the webpage

search = driver.find_element(By.XPATH,"//*[@id='small-searchterms']")
print("Display status: ", search.is_displayed())

# is_enabled - checks if the element is enabled for interaction

print("Enabled status: ", search.is_enabled())

# is_selected - checks if checkbox, radiobutton, or dropdown is selected

rd_button_male = driver.find_element(By.XPATH, "//input[@id = 'gender-male']")
rd_button_female = driver.find_element(By.XPATH, "//input[@id = 'gender-female']")

print("Default radio button status:")
print(rd_button_male.is_selected()) # False
print(rd_button_female.is_selected()) # False

rd_button_male.click() # Selecting male radio button

print("After selecting the male radio button")
print(rd_button_male.is_selected()) # True
print(rd_button_female.is_selected()) # False

rd_button_female.click() # Selecting female radio button, deselects male and selects female

print("After selecting the female radio button")
print(rd_button_male.is_selected()) # False
print(rd_button_female.is_selected()) # True

# Keep browser open
input("Press Enter to close the browser...")

# Close browser
driver.quit()
