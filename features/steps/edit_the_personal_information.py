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
    context.driver.find_element(By.ID,"email-2").send_keys("akhi_27@hotmail.com")
    context.driver.find_element(By.ID, "field").send_keys("abc123")
    context.driver.find_element(By.CSS_SELECTOR, ".login-button.w-button").click()
    sleep(3)

@when('Click on settings option')
def click_settings(context):
    context.driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > a:nth-child(16) > div:nth-child(2)").click()

@when('Click on Edit profile option')
def click_edit_profile(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href='/profile-edit']").click()
    sleep(2)

@then('some test information in the input fields')
def test_inputs(context):
    context.app.edit_profile.test_inputs()

@then('Check the right information is present in the input fields')
def check_inputs(context):
    actual_result = context.driver.find_element(By.CSS_SELECTOR,"#Company-name").get_attribute("value")
    expected_result = 'Test_1'
    assert expected_result in actual_result, f"Expected {expected_result}, got actual {actual_result}"


@then('Check “Close” and “Save Changes” buttons are available and clickable')
def check_and_save_buttons(context):
    context.driver.find_element(By.CSS_SELECTOR,"div[class='save-changes-button']").click()

