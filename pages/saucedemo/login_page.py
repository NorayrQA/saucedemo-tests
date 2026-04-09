import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    SUCCESS_MESSAGE = (By.CLASS_NAME, 'app_logo')

    def open(self):
        self.load(self.URL)

    def type_username(self, username):
        self.bot.type(self.USERNAME, username)

    def type_password(self, password):
        self.bot.type(self.PASSWORD, password)

    def click_login_button(self):
        self.bot.click(self.LOGIN_BUTTON)

    def is_inventory_page_opened(self) -> bool:
        return (
            "inventory" in self.driver.current_url and
            self.is_element_present(self.INVENTORY_CONTAINER)
        )

    def is_logged_in(self, step_name: str | None = None) -> bool:
        label = self._resolve_step_name(
            step_name,
            'Check if user is already logged in'
        )

        with allure.step(label):
            return self.is_inventory_page_opened()

    def login(self, username, password, step_name: str | None = None):
        label = self._resolve_step_name(
            step_name,
            f'Login as user: {username}'
        )

        with allure.step(label):
            self.open()
            self.type_username(username)
            self.type_password(password)
            self.click_login_button()

    def get_error_message(self, step_name: str | None = None) -> str | None:
        return  self.bot.element_text(self.ERROR_MESSAGE, step_name)

