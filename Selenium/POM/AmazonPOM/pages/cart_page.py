from selenium.webdriver.common.by import By
from Selenium.POM.AmazonPOM.pages.base_page import BasePage

# Checkout page
class CartPage(BasePage):
    CART_ICON = (By.ID, "nav-cart")
    PROCEED_TO_CHECKOUT = (By.NAME, "proceedToRetailCheckout")

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_cart(self):
        self.click(self.CART_ICON)

    def proceed_to_checkout(self):
        self.click(self.PROCEED_TO_CHECKOUT)
