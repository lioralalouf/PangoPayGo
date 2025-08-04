
import pytest
from ui.pageObjects.DashboardPage import DashboardPage
from ui.pageObjects.LoginPage import LoginPage
from ui.pageObjects.Navbar import Navbar
from ui.tests.BaseTestUI import BaseTest

@pytest.mark.usefixtures("init_driver")

class TestLoginPage(BaseTest):
    def test_login_valid_user(self, users):

        #Login with valid credentials
        login_page = LoginPage(self.driver)
        username = users["user1"]["username"]
        password = users["user1"]["password"]
        login_page.login(username, password)

        #Verify you have been navigated to dashboard page successfully
        dashboard_page = DashboardPage(self.driver)
        assert dashboard_page.is_loaded(), "Dashboard page did not load correctly"

    def test_password_toggle_visibility(self):
        navbar = Navbar(self.driver)
        navbar.click_nav_link_by_text("logout")
        #Type password when toggle is active - verify password is displayed
        login_page = LoginPage(self.driver)
        login_page.input_password()
        assert login_page.get_password_input_type() == "password"

        #Update toggle to not active - verify password is hidden
        login_page.toggle_password_visibility()
        assert login_page.get_password_input_type() == "text"

        # Make toggle active again - verify password is displayed
        login_page.toggle_password_visibility()
        assert login_page.get_password_input_type() == "password"
