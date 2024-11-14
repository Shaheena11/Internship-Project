from pages.base_page import Page
from pages.edit_profile import EditProfile
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.settings_file_page import Settings


class Application:
    def __init__(self, driver):
        self.page = Page(driver)
        self.edit_profile = EditProfile(driver)
        self.main_page = MainPage(driver)
        self.login_page = LoginPage(driver)
        self.settings_file_page = Settings(driver)

