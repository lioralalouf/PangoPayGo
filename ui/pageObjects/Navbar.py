from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from ui.pageObjects.BasePageUI import BasePage

class Navbar(BasePage):
    NAVBAR = (By.CSS_SELECTOR, ".minimal-navbar.mb-4")

    def click_nav_link_by_text(self, text: str):
        navbar = self.wait.until(EC.presence_of_element_located(self.NAVBAR))
        links = navbar.find_elements(By.TAG_NAME, "a")
        for link in links:
            if link.text.strip().lower() == text.strip().lower():
                link.click()
                return
        raise Exception(f"Link with text '{text}' not found in navbar.")
