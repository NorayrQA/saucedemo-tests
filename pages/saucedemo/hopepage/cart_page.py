from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    SHOPPING_CART = (By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')
    CART_ITEM = (By.CLASS_NAME, "inventory_item_name")

    def go_to_the_shopping_cart(self):
        self.bot.click(self.SHOPPING_CART)

    def get_item_name(self):
        return self.bot.element_text(self.CART_ITEM)

