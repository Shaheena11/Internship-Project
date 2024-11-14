from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class Settings(Page):

    def click_settings(context):
        context.driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > a:nth-child(16) > div:nth-child(2)").click()
        sleep(5)

