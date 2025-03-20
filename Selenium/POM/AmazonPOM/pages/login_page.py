from selenium.webdriver.common.by import By
from Selenium.POM.AmazonPOM.pages.base_page import BasePage
import allure

class LoginPage(BasePage):
    EMAIL_INPUT = (By.ID, "ap_email")
    PASSWORD_INPUT = (By.ID, "ap_password")
    SIGNIN_BUTTON = (By.ID, "signInSubmit")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

    @allure.step("Logging into Amazon")
    def login(self, email, password):
        self.enter_text(self.EMAIL_INPUT, email)
        self.click((By.ID, "continue"))
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click(self.SIGNIN_BUTTON)
