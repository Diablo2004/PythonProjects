from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import allure
import os
# Importing necessary page classes
from Selenium.POM.AmazonPOM.pages.base_page import BasePage
from Selenium.POM.AmazonPOM.pages.login_page import LoginPage
from Selenium.POM.AmazonPOM.pages.home_page import HomePage
from Selenium.POM.AmazonPOM.pages.product_page import ProductPage
from Selenium.POM.AmazonPOM.pages.cart_page import CartPage
from Selenium.POM.AmazonPOM.pages.config import USERNAME, PASSWORD
from Selenium.POM.AmazonPOM.pages.log import Logger
if not os.path.exists("allure-results"):
    os.makedirs("allure-results")
# Setup ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

@allure.step("Opening the Amazon website")
def amazon_shopping():
    try:

        # Step 1: Open Amazon & Login
        driver.get("https://www.amazon.com/")
        driver.maximize_window()

        allure.attach(driver.current_url, name="Opened URL", attachment_type=allure.attachment_type.TEXT)
        Logger.log_info("Opened Amazon.")
        login_page = LoginPage(driver)
        login_page.login(USERNAME, PASSWORD)
        Logger.log_info("Logged in.")
        time.sleep(2)

        # Step 2: Search for a Product

        home_page = HomePage(driver)
        home_page.search_product("cooker")
        time.sleep(2)

        # Step 3: Select a Product & Add to Cart
        product_page = ProductPage(driver)
        product_page.select_first_product()
        time.sleep(2)
        product_page.add_to_cart()
        time.sleep(2)

        # Step 4: Go to Cart & Proceed to Checkout
        cart_page = CartPage(driver)
        cart_page.go_to_cart()
        time.sleep(2)
        cart_page.proceed_to_checkout()
        time.sleep(2)

        # Verify Checkout Page
        if "Checkout" in driver.title:
            print("Test Passed: Reached Checkout Page")
        else:
            print("Test Failed: Checkout Page Not Reached")

    except Exception as e:
        print(f"An error occurred: {e}")
        Logger.log_error(f"Test failed due to error: {str(e)}")
    finally:
        input("Press Enter to close the browser...")

        driver.quit()
        Logger.log_info("Closed the browser.")

# Run the function
amazon_shopping()

print("Test completed. Run 'allure serve allure-results' to generate the report.")
# Ensure results are generated
os.system("allure generate allure-results --clean -o allure-report")
# Open the report
os.system("allure open allure-report")

