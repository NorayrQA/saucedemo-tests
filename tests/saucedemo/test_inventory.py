from pages.saucedemo.inventory_page import InventoryPage


class TestInventory:
    def test_sort_a_to_z(self, logged_in_driver):
        inventory = InventoryPage(logged_in_driver)

        inventory.bot.select_by_visible_text(
            inventory.SORT_DROPDOWN,
            "Name (A to Z)"
        )

        names = inventory.bot.elements_texts(inventory.ITEM_NAMES)

        assert names == sorted(names)