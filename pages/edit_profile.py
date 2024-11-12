from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class EditProfile(Page):
    COMPANY_NAME = (By.CSS_SELECTOR, '[wized="companyInputProfile"]')

    def test_inputs(self):
        self.wait_for_element_to_appear(*self.COMPANY_NAME)
        company_name_field = self.driver.find_element(*self.COMPANY_NAME)
        company_name_field.clear()
        company_name_field.send_keys('Test_1')
        sleep(2)

