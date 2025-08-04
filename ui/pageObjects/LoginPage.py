from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from ui.pageObjects.BasePageUI import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-message")
    TOGGLE_BUTTON = (By.ID, "togglePassword")

    def __init__(self, driver):
        super().__init__(driver)

    def load(self, base_url="http://localhost:5000"):
        self.driver.get(base_url)

    def login(self, username, password):
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        button = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        print(f"Button displayed? {button.is_displayed()}, enabled? {button.is_enabled()}")
        button.click()

    def input_password(self):
        self.type(self.PASSWORD_INPUT, "abc123")

    def toggle_password_visibility(self):
        self.click(self.TOGGLE_BUTTON)

    def get_password_input_type(self):
        return self.driver.find_element(*self.PASSWORD_INPUT).get_attribute("type")

    def get_error_message(self):
        try:
            return self.get_text(self.ERROR_MESSAGE)
        except:
            return None
