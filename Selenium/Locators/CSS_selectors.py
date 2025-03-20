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

# CSS Selectors combinations:

# 1. Tag and ID combination
# driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("abc")

# 2. Tag and Class combination
# driver.find_element(By.CSS_SELECTOR,"input.inputtext._55r1._6luy").send_keys("abc@gmail.com")

# 3. Tag Attribute - tag-name[attribute = value]
driver.find_element(By.CSS_SELECTOR,"input[aria-label='Email address or phone number']").send_keys("abc@gmail.com")

# 4. Tag, Class and Attribute - tag-name.valueOfClass[attribute = value]
#driver.find_element(By.CSS_SELECTOR,"input.inputtext[id = 'pass']").send_keys("xyz")

# Keep browser open
input("Press Enter to close the browser...")

# Close browser
driver.quit()
