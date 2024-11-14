from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class LoginPage(Page):
    EMAIL_LOC = (By.ID, "email-2")
    EMAIL = 'akhi_27@hotmail.com'
    PASSWORD_LOC = (By.ID, "field")
    PASSWORD = "abc123"
    CONFIRM_BTN = (By.CSS_SELECTOR, ".login-button.w-button")

    def login_page(self):
        sleep(2)
        self.find_element(*self.EMAIL_LOC).send_keys(self.EMAIL)
        sleep(2)
        self.find_element(*self.PASSWORD_LOC).send_keys(self.PASSWORD)
        sleep(2)
        self.wait_and_click(*self.CONFIRM_BTN)
        sleep(5)

