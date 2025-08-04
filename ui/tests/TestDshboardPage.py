
import pytest
from ui.pageObjects.DashboardPage import DashboardPage
from ui.pageObjects.LoginPage import LoginPage
from ui.pageObjects.Navbar import Navbar
from ui.tests.BaseTestUI import BaseTest

@pytest.mark.usefixtures("init_driver")

class TestDashboardPage(BaseTest):
    def test_duplicated_parking(self, users, user_data, error_messages):
        login_page = LoginPage(self.driver)

        #Login to lot manager with valid credentials
        username = users["user1"]["username"]
        password = users["user1"]["password"]
        login_page.login(username, password)

        dashboard_page = DashboardPage(self.driver)

        #Fill in all fields for register a newd parking
        car_plate = user_data["valid_car_plate"]
        vehicle_type_id = user_data["vehicle_type_id_option1"]
        slot = user_data["valid_parking_slot"]

        #Delete All active parking's before you add a new one
        dashboard_page.finish_all_active_parkings()

        #Submit the new parking
        dashboard_page.car_parking(car_plate, vehicle_type_id, slot)

        #Verify new parking has been saved
        expected_car_plate = car_plate
        assert dashboard_page.verify_parking_data(expected_car_plate), f"License plate {expected_car_plate} not found"

        #Log out from lot manager dashboard
        navbar = Navbar(self.driver)
        navbar.click_nav_link_by_text("logout")

        #Login with another admin user
        username = users["user2"]["username"]
        password = users["user2"]["password"]
        login_page.login(username, password)

        #Register a new parking with same car plate
        dashboard_page.car_parking(car_plate, vehicle_type_id, slot)

        #Verify correct alert message is displayed to the user
        actual_alert_msg = dashboard_page.get_alert_text(".alert.alert-warning.alert-dismissible.fade.show")
        expected_alert_msg = error_messages["vehicle_already_parked"]
        assert actual_alert_msg == expected_alert_msg, f"Expected: {expected_alert_msg}, Got: {actual_alert_msg}"

    def test_end_parking_successfully(self, users, user_data):
        navbar = Navbar(self.driver)
        navbar.click_nav_link_by_text("logout")
        # Login to lot manager with valid credentials and fill data for new parking
        login_page = LoginPage(self.driver)
        username = users["user1"]["username"]
        password = users["user1"]["password"]
        login_page.login(username, password)
        dashboard_page = DashboardPage(self.driver)
        car_plate = user_data["valid_car_plate"]
        vehicle_type_id = user_data["vehicle_type_id_option1"]
        slot = user_data["valid_parking_slot"]

        #Clear all active parking registrations and register a new parking
        dashboard_page.finish_all_active_parkings()
        dashboard_page.car_parking(car_plate, vehicle_type_id, slot)

        #End parking and verify alert includes the correct car plate
        dashboard_page.end_parking()
        alert_text = dashboard_page.get_alert_text('[role="alert"]')
        expected_car_plate = car_plate
        assert expected_car_plate in alert_text, f"Expected code '{expected_car_plate}' not found in alert text: '{alert_text}'"








