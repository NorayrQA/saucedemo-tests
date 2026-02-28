from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")
    ADD_TO_CART = (By.ID, 'add-to-cart-sauce-labs-onesie')

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

    def get_all_prices(self):
        prices_text = self.bot.elements_texts(
            self.PRODUCT_PRICES,
            step_name="Get all product prices"
        )
        return [float(price.replace("$", "")) for price in prices_text]

    def click_add_to_cart_button(self):
        self.bot.click(self.ADD_TO_CART, step_name="Add to cart")



