from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))

    def click(self, by_locator):
        self.find(by_locator).click()

    def enter_text(self, by_locator, text):
        self.find(by_locator).send_keys(text)

    def wait_for_title(self, title, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.title_is(title))
