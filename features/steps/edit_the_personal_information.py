from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open the main page https://soft.reelly.io')
def open_reelly(context):
    # context.driver.get('https://soft.reelly.io')
    context.app.main_page.open_main_page()
    sleep(3)


@when('Log in to the page')
def log_in_page(context):
    context.app.login_page.login_page()

@when('Click on settings option')
def click_settings(context):
    context.app.settings_file_page.click_settings()


@when('Click on Edit profile option')
def click_edit_profile(context):
    context.app.edit_profile.click_edit_profile()

@then('some test information in the input fields')
def test_inputs(context):
    context.app.edit_profile.test_inputs()

@then('Check the right information is present in the input fields')
def check_inputs(context):
    context.app.edit_profile.check_inputs()

@then('Check “Close” and “Save Changes” buttons are available and clickable')
def check_and_save_buttons(context):
    context.app.edit_profile.check_and_save_buttons()

