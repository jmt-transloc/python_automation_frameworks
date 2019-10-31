from attrdict import AttrDict
from selenium.webdriver.common.by import By

import config


_constants = AttrDict({
    "BASE_PAGE": {
        "URL": config.options.URL
    },
    "SEARCH_PAGE": {
        "INPUT": (By.NAME, 'q')
    },
    "RESULTS_PAGE": {
        "DIVS": (By.CLASS_NAME, 'rc'),
        "INPUT": (By.NAME, 'q')
    }
})


# class BasePage:
#     URL = config.options.URL
#
#
# class SearchPage:
#     INPUT = (By.NAME, 'q')
#
#
# class ResultsPage:
#     DIVS = (By.CLASS_NAME, 'rc')
#     INPUT = (By.NAME, 'q')
