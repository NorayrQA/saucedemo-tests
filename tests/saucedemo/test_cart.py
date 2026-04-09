from pages.saucedemo.inventory_page import InventoryPage
from pages.saucedemo.cart_page import CartPage


class TestCart:
    def test_add_to_cart(self, logged_in_driver):
        inventory = InventoryPage(logged_in_driver)
        cart = CartPage(logged_in_driver)

        inventory.add_first_item_to_cart()
        assert inventory.get_cart_count() == 1

        cart.remove_item()
        assert inventory.get_cart_count() == 0


    def test_open_cart(self, logged_in_driver):
        inventory = InventoryPage(logged_in_driver)
        inventory.add_first_item_to_cart()
        inventory.open_cart()

        cart = CartPage(logged_in_driver)
        cart.wait_until_loaded()
        assert cart.get_items_count() == 1