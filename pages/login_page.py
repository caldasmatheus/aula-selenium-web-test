# pages/login_page.py

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.XPATH, "//div[@class='error-message-container error']")
    PRODUCTS_TITLE = (By.CLASS_NAME, "title")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://www.saucedemo.com")

    def login(self, username, password):
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.find(self.ERROR_MESSAGE).text

    def is_login_successful(self, expected_title):
        self.wait_for_title(expected_title)
        return self.driver.title == expected_title

    def is_on_products_page(self):
        return self.find(self.PRODUCTS_TITLE).text == "Products"
