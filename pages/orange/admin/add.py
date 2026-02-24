from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AdminAddPage(BasePage):
    ADMIN_PAGE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers"
    LEFT_MENU_ADMIN_ITEM = (By.CSS_SELECTOR, "a[href='/web/index.php/admin/viewAdminModule']")
    ADD_BUTTON = (By.XPATH, "//button[normalize-space()='Add']")
    USER_ROLE_DROPDOWN = (
        By.XPATH,
        "(//label[normalize-space()='User Role']"
        "/ancestor::div[contains(@class,'oxd-input-group')]"
        "//div[contains(@class,'oxd-select-wrapper')]"
        "//div[contains(@class,'oxd-select-text')])[1]"
    )

    USER_ROLE_DROPDOWN_INPUT = (
        By.XPATH,
        "//label[normalize-space()='User Role']"
        "/ancestor::div[contains(@class,'oxd-input-group')]"
        "//div[contains(@class,'oxd-select-text-input')]"
    )

    USER_ROLE_ADMIN_OPTION = (
        By.XPATH,
        "//div[contains(@class,'oxd-select-dropdown')]//span[normalize-space()='Admin']"
    )

    def page_load(self):
        self.load(self.ADMIN_PAGE_URL)

    def click_left_menu_admin_item_button(self) -> None:
        self.bot.click(self.LEFT_MENU_ADMIN_ITEM)

    def click_add_button(self) -> None:
        self.bot.click(self.ADD_BUTTON)

    def select_user_role_admin(self) -> None:
        self.bot.click(self.USER_ROLE_DROPDOWN_INPUT, step_name='Open User Role dropdown')
        self.bot.click(self.USER_ROLE_ADMIN_OPTION, step_name='Select Admin from User Role')