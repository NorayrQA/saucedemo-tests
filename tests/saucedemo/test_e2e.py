from pages.saucedemo.login_page import LoginPage
from pages.saucedemo.inventory_page import InventoryPage
from pages.saucedemo.cart_page import CartPage
from pages.saucedemo.checkout_page import CheckoutPage


class TestE2E:

    def test_full_user_flow(self, driver):
        login = LoginPage(driver)
        login.login("standard_user", "secret_sauce")

        inventory = InventoryPage(driver)
        inventory.add_first_item_to_cart()
        inventory.open_cart()

        cart = CartPage(driver)
        cart.wait_until_loaded()
        cart.click_checkout()

        checkout = CheckoutPage(driver)
        checkout.fill_information("John", "Doe", "12345")
        checkout.continue_checkout()
        checkout.finish_checkout()

        assert checkout.get_success_message() == "Thank you for your order!"