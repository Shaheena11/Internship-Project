from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class EditProfile(Page):
    COMPANY_NAME = (By.CSS_SELECTOR, '[wized="companyInputProfile"]')

    def click_edit_profile(context):
        context.driver.find_element(By.CSS_SELECTOR, "a[href='/profile-edit']").click()
        sleep(5)

    def test_inputs(self):
        self.wait_until_clickable(*self.COMPANY_NAME)
        company_name_field = self.driver.find_element(*self.COMPANY_NAME)
        company_name_field.clear()
        company_name_field.send_keys('Test_1')
        sleep(2)

    def check_inputs(context):
        actual_result = context.driver.find_element(By.CSS_SELECTOR, "#Company-name").get_attribute("value")
        expected_result = 'Test_1'
        assert expected_result in actual_result, f"Expected {expected_result}, got actual {actual_result}"

    def check_and_save_buttons(context):
        context.driver.find_element(By.CSS_SELECTOR,"div[class='save-changes-button']").click()
