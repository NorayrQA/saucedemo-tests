from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    ADD_TO_CART_BUTTONS = (By.XPATH, "//button[contains(text(),'Add to cart')]")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    ERROR_MESSAGE = (By.XPATH, '//h3[@data-test="error"]')
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")


    def is_loaded(self) -> bool:
        return self.is_element_present(self.INVENTORY_ITEMS)

    def add_first_item_to_cart(self):
        self.bot.click(self.ADD_TO_CART_BUTTONS)

    def get_cart_count(self) -> int:
        if not self.is_element_present(self.CART_BADGE):
            return 0
        return int(self.bot.element_text(self.CART_BADGE))

    def open_cart(self):
        self.bot.click(self.CART_LINK)

    def logout(self):
        self.bot.click(self.MENU_BUTTON)
        self.bot.click(self.LOGOUT_LINK)
