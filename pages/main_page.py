from selenium.webdriver.common.by import By
from pages.base_page import Page


class MainPage(Page):
    #
    # CART_BUTTON = (By.CSS_SELECTOR, '[data-test="@web/CartLink"]')
    # CART_EMPTY = (By.CSS_SELECTOR, "div[class='sc-5da3fdcc-0 ChXCV']")
    MAIN_MENU = (By.XPATH, "//a[contains(@class, 'assistant-button')] //div[@class='circle-gradient']")
    PROFILE_ICON = (By.XPATH, "//a[@href='/settings' and @class='menu-photo_avatar w-inline-block']")

    def open_main_page(self):
        self.open('https://soft.reelly.io')


    def click_on_Main_Menu(self):
        self.wait_and_click(*self.MAIN_MENU)


    def click_on_Profile_icon(self):
        self.wait_and_click(*self.PROFILE_ICON)

    # def click_cart(self):
    #     self.click(*self.CART_BUTTON)
    #
    # def cart_is_empty(self):
    #     actual_result = self.driver.find_element(*self.CART_EMPTY).text
    #     expected_result = 'Your cart is empty'
    #     assert expected_result in actual_result, f'Expected {expected_result}, got actual {actual_result}'

