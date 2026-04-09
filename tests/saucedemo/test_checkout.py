from pages.saucedemo.inventory_page import InventoryPage
from pages.saucedemo.cart_page import CartPage
from pages.saucedemo.checkout_page import CheckoutPage


class TestCheckout:

    def test_success_checkout(self, logged_in_driver):
        inventory = InventoryPage(logged_in_driver)
        inventory.add_first_item_to_cart()
        inventory.open_cart()

        cart = CartPage(logged_in_driver)
        cart.click_checkout()

        checkout = CheckoutPage(logged_in_driver)
        checkout.fill_information("John", "Doe", "12345")
        checkout.continue_checkout()
        checkout.finish_checkout()

        assert checkout.get_success_message() == "Thank you for your order!"


    def test_checkout_empty_fields(self, logged_in_driver):
        inventory = InventoryPage(logged_in_driver)
        inventory.add_first_item_to_cart()
        inventory.open_cart()

        cart = CartPage(logged_in_driver)
        cart.click_checkout()

        checkout = CheckoutPage(logged_in_driver)
        checkout.continue_checkout()

        assert "Error" in logged_in_driver.page_source

    def test_checkout_missing_last_name(self, logged_in_driver):
        inventory = InventoryPage(logged_in_driver)
        inventory.add_first_item_to_cart()
        inventory.open_cart()

        cart = CartPage(logged_in_driver)
        cart.wait_until_loaded()
        cart.click_checkout()

        checkout = CheckoutPage(logged_in_driver)
        checkout.wait_until_loaded()

        checkout.fill_information("John", "", "12345")
        checkout.continue_checkout()

        assert "Last Name is required" in logged_in_driver.page_source