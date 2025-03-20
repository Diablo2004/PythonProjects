from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.facebook.com/") # opening the browser with get
driver.maximize_window() # maximize the browser window

wait = WebDriverWait(driver, 10)

# Absolute XPath
# driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input").send_keys("abc@gmail.com")
# driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input").send_keys("abc")

# Relative XPath
# login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@name='login']")))
# login_button.click()

# or
# driver.find_element(By.XPATH,"//input[@id = 'email' or @name = 'email']").send_keys("abc@gmail.com")

# and
# driver.find_element(By.XPATH,"//input[@id = 'pass' and @name = 'pass']").send_keys("abc")

# contains()
# driver.find_element(By.XPATH,"//input[contains(@placeholder, 'address')]").send_keys("abc")

# starts-with()
# driver.find_element(By.XPATH,"//input[starts-with(@placeholder, 'Email')]").send_keys("abc")

# text()
driver.find_element(By.XPATH,"//a[text() = 'Forgotten password?']").click()
input("Press Enter to close the browser...")

# Close browser
driver.quit()
