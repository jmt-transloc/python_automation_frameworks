import json
import pytest
from selenium.webdriver import Chrome

from tests.config import parse_env_variables, parse_json_variables, options

CONFIG_PATH = 'tests/config.json'
DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSERS = ['chrome']

#
# Configure the environment for automation
#
parse_env_variables()
parse_json_variables()


@pytest.fixture(scope='session')
def config():
    """ Pull and return data from a configuration file """

    with open(CONFIG_PATH) as config_file:
        data = json.load(config_file)
    return data


@pytest.fixture(scope='session')
def config_browser(config):
    """ Define a browser based on configuration files """

    if 'browser' not in config:
        raise Exception('The configuration file does not contain "browser"')
    elif config['browser'] not in SUPPORTED_BROWSERS:
        raise Exception(f'"{config["browser"]}" is not a supported browser')
    return config['browser']


@pytest.fixture(scope='session')
def config_wait_time(config):
    """ Define a wait time based on configuration files """
    return config['wait_time'] if 'wait_time' in config else DEFAULT_WAIT_TIME


@pytest.fixture
def browser(config_browser, config_wait_time):
    """ Create a browser and actions using config fixtures """

    if config_browser == 'chrome':
        driver = Chrome()
    else:
        raise Exception(
            f'"{config["browser"]}" is not a supported browser'
        )

    driver.implicitly_wait(config_wait_time)

    yield driver

    options.clear()
    driver.quit()
