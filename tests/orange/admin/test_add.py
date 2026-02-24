from selenium.webdriver.remote.webdriver import WebDriver
from pages.orange.admin.add import AdminAddPage


class TestAdminAdd:
    def test_add_success(self, logged_in_driver: WebDriver):
        add_page = AdminAddPage(logged_in_driver)
        add_page.click_left_menu_admin_item_button()
        add_page.click_add_button()
        add_page.select_user_role_admin()