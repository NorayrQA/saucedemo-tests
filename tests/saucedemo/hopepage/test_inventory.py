from pages.saucedemo.hopepage.cart_page import CartPage
from pages.saucedemo.hopepage.inventory_page import InventoryPage

class TestSelectPrice:

    def test_select_price_page(self, logged_in_driver):
        inventory = InventoryPage(logged_in_driver)

        inventory.select_sort_by_value("lohi")

        assert inventory.get_selected_sort_option() == "Price (low to high)"


    def test_sort_prices_low_to_high(self, logged_in_driver):
        inventory_page = InventoryPage(logged_in_driver)

        inventory_page.select_sort_by_value("lohi")

        prices = inventory_page.get_all_prices()

        assert len(prices) > 1
        assert prices == sorted(prices)

    def test_add_to_cart(self, logged_in_driver):
        inventory_page = InventoryPage(logged_in_driver)
        cart_page = CartPage(logged_in_driver)

        inventory_page.click_add_to_cart_button()

        cart_page.go_to_the_shopping_cart()

        print(cart_page.get_item_name())