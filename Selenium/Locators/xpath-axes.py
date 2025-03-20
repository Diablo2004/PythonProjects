from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://money.rediff.com/gainers/bse/daily/groupa") # opening the browser with get
driver.maximize_window() # maximize the browser window

#self

text_msg = driver.find_element(By.XPATH,"//a[contains(text(),'KSB')]/self::a").text
print(text_msg) # Expected output = KSB

# parent
# text_msg = driver.find_element(By.XPATH,"//a[contains(text(),'KSB')]/parent::td").text
# print(text_msg) # Expected output = KSB

# child
# childs = driver.find_elements(By.XPATH,"//a[contains(text(),'KSB')]/ancestor::tr/child::td") # all child of ancestor node
# print(len(childs)) # Expected output = 6

# ancestor
# ancestor = driver.find_element(By.XPATH,"//a[contains(text(),'KSB')]/ancestor::tr").text # all ancestor node
# print(ancestor) # Expected output = KSB A 609.25 622.00 + 2.09 Buy  |  Sell

# descendant
# dec = driver.find_elements(By.XPATH,"//a[contains(text(),'KSB')]/ancestor::tr/descendant::*") # all descendant of ancestor node
# print(len(dec)) # Expected output = 10

# following
# fol = driver.find_elements(By.XPATH,"//a[contains(text(),'KSB')]/ancestor::tr/following::*") # all following nodes of ancestor node
# print(len(fol)) # Expected output = 929

# following-siblings
# siblings = driver.find_elements(By.XPATH,"//a[contains(text(),'KSB')]/ancestor::tr/following-sibling::*") # all following-siblings of ancestor node
# print(len(siblings)) # Expected output = 64

# preceding
# preceding = driver.find_elements(By.XPATH,"//a[contains(text(),'KSB')]/ancestor::tr/preceding::*") # all preceding of ancestor node
# print(len(preceding)) # Expected output = 627

# preceding-siblings
# precedingsiblings = driver.find_elements(By.XPATH,"//a[contains(text(),'KSB')]/ancestor::tr/preceding-sibling::*") # all child of ancestor node
# print(len(precedingsiblings)) # Expected output = 67

# Keep browser open
input("Press Enter to close the browser...")

# Close browser
driver.quit()
