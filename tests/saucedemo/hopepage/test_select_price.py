from pages.saucedemo.hopepage.select_price_page import SelectPricePage

class TestSelectPrice:

    def test_select_price_page(self, logged_in_driver):
        inventory = SelectPricePage(logged_in_driver)

        inventory.select_sort_by_value("lohi")

        assert inventory.get_selected_sort_option() == "Price (low to high)"