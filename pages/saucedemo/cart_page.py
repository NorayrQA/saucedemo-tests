from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    REMOVE_BUTTON = (By.CSS_SELECTOR, "[data-test^='remove']")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")

    def wait_until_loaded(self):
        self.wait_for_element_visible(self.CART_ITEMS)

    def get_item_names(self) -> list[str]:
        return self.bot.elements_texts(self.ITEM_NAMES)

    def remove_item(self):
        self.bot.click(self.REMOVE_BUTTON)

    def get_items_count(self) -> int:
        return len(self.find_elements(self.CART_ITEMS))

    def click_checkout(self):
        self.bot.click(self.CHECKOUT_BUTTON)

    def is_cart_empty(self) -> bool:
        return self.get_items_count() == 0

