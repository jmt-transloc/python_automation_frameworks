from selenium.webdriver.common.by import By

import os


class BasePage:
    URL = 'https://www.' + os.getenv('ENV') + '.com'


class SearchPage:
    INPUT = (By.NAME, 'q')


class ResultsPage:
    DIVS = (By.CLASS_NAME, 'rc')
    INPUT = (By.NAME, 'q')
