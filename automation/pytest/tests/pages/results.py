from tests.support.constants import ResultsPage


class GoogleResultsPage:
    _result_divs = ResultsPage.DIVS
    _search_field = ResultsPage.INPUT

    def __init__(self, browser):
        self.browser = browser

    #
    # Page Elements
    #
    def search_field(self):
        return self.browser.find_element(*self._search_field)

    #
    # Page Methods
    #
    def result_div_count(self):
        result_divs = self.browser.find_elements(*self._result_divs)
        return len(result_divs)

    # noinspection PyMethodMayBeStatic
    def search_input_value(self, search_field):
        """
        A method for returning the value of a specific field
        @param search_field - A text field which is scraped for its value in testing
        @return - The value of the text field passed into the method
        """
        return search_field.get_attribute('value')
