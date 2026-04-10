from pages.saucedemo.login_page import LoginPage
from tests.conftest import driver
from utils import constants
import pytest


class TestLogin:
    def test_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()

        login_page.login(
            username=constants.LOGIN_USERNAME,
            password=constants.LOGIN_PASSWORD
        )

        assert login_page.is_inventory_page_opened(), "Inventory page is not opened"


    @pytest.mark.parametrize(
        "username, password, expected",
        [
            pytest.param('standard_user', 'Wrong_pass',
                         'Epic sadface: Username and password do not match any user in this service',
                         id='wrong password'),
            pytest.param('wrong_user', 'secret_sauce',
                         'Epic sadface: Username and password do not match any user in this service',
                         id='wrong username'),
            pytest.param('', 'secret_sauce',
                         'Epic sadface: Username is required',
                         id='empty username'),
            pytest.param('standard_user', '',
                         'Epic sadface: Password is required',
                         id='empty password'),
        ]
    )
    def test_invalid_login(self, driver, username, password, expected):
        login_page = LoginPage(driver)
        login_page.login(username=username, password=password)

        assert login_page.get_error_message() == expected


    def test_locked_user(self, driver):
        login = LoginPage(driver)

        login.login("locked_out_user", "secret_sauce")

        assert "locked out" in login.get_error_message().lower()
