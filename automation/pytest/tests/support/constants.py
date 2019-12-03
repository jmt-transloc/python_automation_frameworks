from selenium.webdriver.common.by import By

from tests import config


class BasePage:
    URL = config.options.URL


class SearchPage:
    INPUT = (By.NAME, 'q')


class ResultsPage:
    DIVS = (By.CLASS_NAME, 'rc')
    INPUT = (By.NAME, 'q')
