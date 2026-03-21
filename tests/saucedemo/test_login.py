from pages.saucedemo.login_page import LoginPage
from tests.conftest import driver
from utils import constants


class TestLogin:
    def test_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()

        login_page.login(
            username=constants.LOGIN_USERNAME,
            password=constants.LOGIN_PASSWORD
        )

        assert login_page.is_inventory_page_opened(), "Inventory page is not opened"
