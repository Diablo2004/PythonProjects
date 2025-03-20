from selenium.webdriver.common.by import By
from Selenium.POM.AmazonPOM.pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# This page selects the first product from search results and adds it to the cart.

class ProductPage(BasePage):
    FIRST_PRODUCT = (By.XPATH, "(//div[@data-component-type='s-search-result']/div/div/div/div/span/div/div/div/div[2]/div/div/div/a)[1]")
    ADD_TO_CART = (By.ID, "add-to-cart-button")

    def __init__(self, driver):
        super().__init__(driver)

    def select_first_product(self):
        self.click(self.FIRST_PRODUCT)

    def add_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ADD_TO_CART)
        ).click()
        print("Clicked on Add to Cart")
