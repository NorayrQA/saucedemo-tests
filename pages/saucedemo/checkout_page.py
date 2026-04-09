from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "complete-header")

    def fill_information(self, first_name, last_name, postal_code):
        self.bot.type(self.FIRST_NAME, first_name)
        self.bot.type(self.LAST_NAME, last_name)
        self.bot.type(self.POSTAL_CODE, postal_code)

    def continue_checkout(self):
        self.bot.click(self.CONTINUE_BUTTON)

    def finish_checkout(self):
        self.bot.click(self.FINISH_BUTTON)

    def get_success_message(self) -> str:
        return self.bot.element_text(self.SUCCESS_MESSAGE)

    def wait_until_loaded(self):
        self.wait_for_element_visible(self.FIRST_NAME)