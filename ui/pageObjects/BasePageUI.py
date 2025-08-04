import logging
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = logging.getLogger(self.__class__.__name__)

    def click(self, locator):
        self.logger.info(f"Trying to click element: {locator}")
        self.wait.until(EC.element_to_be_clickable(locator)).click()
        self.logger.info(f"Clicked element: {locator}")

    def navigate_to_tab(self, locator, txt1, txt2):
        try:
            self.logger.debug(f"Before click - current URL: {self.driver.current_url}")

            el = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, locator))
            )
            el.click()
            self.logger.info(f"Clicked tab element: {locator}")

            WebDriverWait(self.driver, 10).until(
                lambda driver: txt1 in driver.current_url or txt2 in driver.current_url
            )

            self.logger.debug(f"Navigation successful - current URL: {self.driver.current_url}")
            return self.driver.current_url

        except Exception as e:
            self.logger.error(f"Failed to navigate to tab: {e}")
            return None

    def type(self, locator, text):
        self.logger.info(f"Typing into element: {locator} text: {text}")
        el = self.wait.until(EC.visibility_of_element_located(locator))
        el.clear()
        el.send_keys(text)
        self.logger.info(f"Typed text into element: {locator}")

    def get_text(self, locator):
        try:
            el = self.wait.until(EC.visibility_of_element_located(locator))
            text = el.text
            self.logger.info(f"Got text from element {locator}: {text}")
            return text
        except TimeoutException:
            self.logger.error(f"Timeout while waiting for element {locator} to be visible for getting text")
            return None

    def get_current_url(self):
        url = self.driver.current_url
        self.logger.info(f"Current URL: {url}")
        return url

    def is_displayed(self, locator):
        try:
            displayed = self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
            self.logger.info(f"Element {locator} displayed: {displayed}")
            return displayed
        except TimeoutException:
            self.logger.warning(f"Element {locator} not displayed (timeout)")
            return False

    def scroll_into_view(self, locator):
        self.logger.info(f"Scrolling into view element: {locator}")
        el = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", el)
        self.logger.info(f"Scrolled into view element: {locator}")

    def scroll_to_element(self, locator):
        """
        גולל את המסך עד שהאלמנט יהיה בטווח הגלוי באמצעות תנועת עכבר.
        """
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            self.logger.info(f"Scrolled to element: {locator}")
        except Exception as e:
            self.logger.error(f"Failed to scroll to element {locator}: {e}")
