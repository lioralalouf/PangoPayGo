from selenium.common import TimeoutException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from ui.pageObjects.BasePageUI import BasePage

class DashboardPage(BasePage):
    DASHBOARD_HEADER = (By.CSS_SELECTOR, ".dashboard-header")
    CAR_PLATE = (By.ID, "car_plate")
    VEHICLE_TYPE_SELECT = (By.ID, "vehicle_type_id")
    SLOT = (By.ID, "slot")
    SUBMIT_BUTTON = (By.ID, "submit")
    PARKING_DATA = (By.CSS_SELECTOR, "table tbody tr")
    END_PARKING = (By.CSS_SELECTOR, ".btn.btn-danger.btn-sm")

    def is_loaded(self):
        try:
            el = self.wait.until(EC.visibility_of_element_located(self.DASHBOARD_HEADER))
            text = el.text
            self.logger.info(f"Dashboard header text: {text}")
            return "חניות פעילות נוכחיות" in text
        except TimeoutException:
            self.logger.error("Dashboard header not found!")
            self.logger.error(f"Current URL: {self.driver.current_url}")
            return False

    def car_parking(self, car_plate, vehicle_type_text, slot):
        self.logger.info(f"Filling car parking form: plate={car_plate}, type={vehicle_type_text}")

        self.type(self.CAR_PLATE, car_plate)

        select_element = self.driver.find_element(*self.VEHICLE_TYPE_SELECT)
        select = Select(select_element)
        select.select_by_visible_text(vehicle_type_text)
        self.logger.info(f"Selected vehicle type: {vehicle_type_text}")

        self.type(self.SLOT, slot)

        self.click(self.SUBMIT_BUTTON)
        self.logger.info("Clicked submit button")

    def finish_all_active_parkings(self):
        rows = self.driver.find_elements(By.CSS_SELECTOR, "table tbody tr")
        while rows:
            try:
                first_row = rows[0]
                finish_button = first_row.find_element(By.XPATH, ".//button[contains(text(), 'סיים')]")
                finish_button.click()
                self.logger.info("Clicked 'סיים' button on a parking record.")
                self.wait.until(lambda driver: len(driver.find_elements(By.CSS_SELECTOR, "table tbody tr")) < len(rows))
                rows = self.driver.find_elements(By.CSS_SELECTOR, "table tbody tr")  # עדכון רשומות אחרי לחיצה
            except StaleElementReferenceException:
                self.logger.warning("Stale element caught, refreshing rows...")
                rows = self.driver.find_elements(By.CSS_SELECTOR, "table tbody tr")
            except Exception as e:
                self.logger.error(f"Error: {e}")
                break

    def verify_parking_data(self, expected_license):
        rows = self.driver.find_elements(By.CSS_SELECTOR, "table tbody tr")
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            for cell in cells:
                if expected_license in cell.text:
                    self.logger.info(f"License plate {expected_license} found in cell: {cell.text}")
                    return True
        self.logger.warning(f"License plate {expected_license} not found in table.")
        return False

    def get_alert_text(self,el):
        try:
            alert_element = self.wait.until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, el)
                )
            )
            return alert_element.text.strip()
        except:
            return None

    def end_parking(self):
        rows = self.driver.find_elements(By.CSS_SELECTOR, "table tbody tr")
        if not rows:
            self.logger.warning("No active parking rows found.")
            return

        try:
            finish_button = rows[0].find_element(By.XPATH, ".//button[contains(text(), 'סיים')]")
            finish_button.click()
            self.logger.info("Clicked 'סיים' on the first row.")
        except Exception as e:
            self.logger.error(f"Error clicking end parking button: {e}")



