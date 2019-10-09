# results
from selenium.webdriver.common.by import By

class GoogleResultsPage:
    RESULT_DIVS = (By.CLASS_NAME, 'rc')
    SEARCH_FIELD = (By.NAME, 'q')
    
    def __init__(self, browser):
        self.browser = browser
        
    def result_div_count(self):
        result_divs = self.browser.find_elements(*self.RESULT_DIVS)
        return len(result_divs)
    
    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_FIELD)
        return search_input.get_attribute('value')
