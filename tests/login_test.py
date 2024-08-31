import os
import json
from dotenv import load_dotenv
import pytest
from selenium import webdriver
from pages.login_page import LoginPage

load_dotenv()

credentials_json = os.getenv("LOGIN_CREDENTIALS")
credentials = json.loads(credentials_json)

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_login_success(driver):
    EXPECTED_TITLE = "Swag Labs"
    user = credentials['login_success']

    login_page = LoginPage(driver)
    login_page.login(user['username'], user['password'])

    assert login_page.is_login_successful(EXPECTED_TITLE)
    assert login_page.is_on_products_page()

def test_login_failure_incorrect_password(driver):
    EXPECTED_ERROR_MESSAGE = "Epic sadface: Username and password do not match any user in this service"
    user = credentials['login_failure_incorrect_password']

    login_page = LoginPage(driver)
    login_page.login(user['username'], user['password'])

    assert login_page.get_error_message() == EXPECTED_ERROR_MESSAGE

def test_login_failure_locked_out_user(driver):
    EXPECTED_ERROR_MESSAGE = "Epic sadface: Sorry, this user has been locked out."
    user = credentials['test_login_failure_locked_out_user']

    login_page = LoginPage(driver)
    login_page.login(user['username'], user['password'])

    assert login_page.get_error_message() == EXPECTED_ERROR_MESSAGE