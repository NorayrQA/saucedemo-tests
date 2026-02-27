from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SelectPricePage(BasePage):

    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")

    def select_sort_by_value(self, value: str) -> None:
        self.bot.select_by_value(
            self.SORT_DROPDOWN,
            value,
            step_name=f"Select sort by value: {value}"
        )

    def get_selected_sort_option(self) -> str:
        return self.bot.get_selected_option_text(
            self.SORT_DROPDOWN,
            step_name="Get selected sort option"
        )