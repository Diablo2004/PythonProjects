from selenium.webdriver.common.by import By
from Selenium.POM.AmazonPOM.pages.base_page import BasePage
import allure
class HomePage(BasePage):
    SEARCH_BOX = (By.ID, "twotabsearchtextbox")
    SEARCH_BUTTON = (By.ID, "nav-search-submit-button")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://www.amazon.com")

    @allure.step("Searching for a product")
    def search_product(self, product_name):
        self.enter_text(self.SEARCH_BOX, product_name)
        self.click(self.SEARCH_BUTTON)
