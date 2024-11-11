from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class EditProfile(Page):
    COMPANY_NAME = (By.CSS_SELECTOR, '[wized="companyInputProfile"]')

    def test_inputs(self):
        sleep(5)
        self.find_element(*self.COMPANY_NAME).clear()
        self.find_element(*self.COMPANY_NAME).send_keys('Test_1')
        sleep(2)
