from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from app.application import Application

def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
   ## Chrome ##
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)


    ## FireFox ##
    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)

    ## Headless Mode ##
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

    ## Browser Stalk ##
    # bs_user = 'shaheenasultana_j0c9Wr'
    # bs_key = 'KqQz1zsbs9q9DxTjxp5q'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # # bstack_options = {
    # #     "os": "Windows",
    # #     "osVersion": "11",
    # #     'browserName': 'chrome',
    # #     'sessionName': scenario_name
    # # }
    # #FOR MOBILE BSTACK OPTIONS
    # bstack_options = {
    #     "deviceName": "Pixel 7",
    #     "platformName": "Android",
    #     'browserName': 'chrome',
    #     'interactiveDebugging': True,
    #     'sessionName': scenario_name
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

    #Mobile Configuration
    mobile_emulation = {
        "deviceName": "Pixel 7"  # Choose a mobile device
    }

    options = webdriver.ChromeOptions()
    options.add_experimental_option("mobileEmulation", mobile_emulation)

    # Initialize WebDriver with mobile emulation
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service, options=options)

    # context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
