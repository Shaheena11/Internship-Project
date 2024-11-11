from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class LoginPage(Page):


    def login_page(self):
        self.open('https://soft.reelly.io/sign-in')
        sleep(3)

