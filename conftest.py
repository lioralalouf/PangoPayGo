import json
import logging
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from api.tests.BaseTestApi import BaseTestApi


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to use: chrome or firefox")
    parser.addoption("--env", action="store", default="prod", help="Environment to run against: prod, staging, or dev")
    parser.addoption("--headless", action="store_true", help="Run tests in headless mode")

#Users Data
@pytest.fixture(scope="function")
def users():
    return {
        "user1": {"username": "admin", "password": "password"},
        "user2": {"username": "administrator", "password": "password2"},
    }

@pytest.fixture(scope="function")
def user_data():
    return {
        "valid_car_plate": "12345679",
        "valid_parking_slot": "23",
        "vehicle_type_id_option1": "Standard"
    }

@pytest.fixture(scope="function")
def error_messages():
    return {
        "vehicle_already_parked":"Duplicate parking prevented: this car is already parked.",
    }

@pytest.fixture(scope="session")
def api_client(request):
    env = request.config.getoption("--env")
    client = BaseTestApi(env=env)
    return client


def pytest_configure():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
        handlers=[logging.StreamHandler()]
    )

@pytest.fixture(scope="class")
def init_driver(request):
    browser = request.config.getoption("--browser").lower()
    env = request.config.getoption("--env").lower()
    headless = request.config.getoption("--headless")

    print(f"\n[INFO] Launching {browser.upper()} browser | Headless: {headless} | Env: {env}")

    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-software-rasterizer")
        options.add_argument("--disable-features=IsolateOrigins,site-per-process")
        options.add_argument("--disable-blink-features=AutomationControlled")

        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--window-size=1920,1080")

        driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)

    else:
        raise ValueError(f"[ERROR] Unsupported browser: {browser}")

    if not headless and browser != "firefox":
        try:
            driver.maximize_window()
        except:
            print("[WARNING] Failed to maximize window")

    request.cls.driver = driver
    request.cls.env = env

    yield

    print("\n[INFO] Quitting driver")
    driver.quit()
