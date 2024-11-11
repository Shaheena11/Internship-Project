from pages.base_page import Page
from pages.edit_profile import EditProfile
from pages.main_page import MainPage


class Application:
    def __init__(self, driver):
        self.page = Page(driver)
        self.edit_profile = EditProfile(driver)
        self.main_page = MainPage(driver)


