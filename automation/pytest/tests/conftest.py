# conftest - Configurations for all tests within the suite
import json
import pytest

from selenium.webdriver import Chrome

CONFIG_PATH = 'tests/config.json'
DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSERS = ['chrome']

#
# Pull and return data from a configuration file
#
@pytest.fixture(scope='session')
def config():
    with open(CONFIG_PATH) as config_file:
        data = json.load(config_file)
    return data

#
# Define a browser based on configuration files
#
@pytest.fixture(scope='session')
def config_browser(config):
    if 'browser' not in config:
        raise Exception('The configuration file does not contain "browser"')
    elif config['browser'] not in SUPPORTED_BROWSERS:
        raise Exception(f'"{config["browser"]}" is not a supported browser')
    return config['browser']

#
# Define a wait time based on configuration files
#
@pytest.fixture(scope='session')
def config_wait_time(config):
    return config['wait_time'] if 'wait_time' in config else DEFAULT_WAIT_TIME

#
# Create a browser and actions using config fixtures
#
@pytest.fixture
def browser(config_browser, config_wait_time):
    
    # Create a browser based on config
    if config_browser == 'chrome':
        driver = Chrome()
    else:
        raise Exception(
            f'"{config["browser"]}" is not a supported browser'
        )

    # Define an implicit wait based on config
    driver.implicitly_wait(config_wait_time)
    
    # Return a driver object for use in objects
    yield driver
    
    # Quit the driver once tests are complete
    driver.quit()
