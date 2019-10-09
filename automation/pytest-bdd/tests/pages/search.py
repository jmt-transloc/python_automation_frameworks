from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pypom import Page


class GoogleSearch(Page):
    test_var = 'Google Search'
    _url = 'https://www.google.com'
    _search_input = (By.NAME, 'q')
    _search_button = (By.CSS_SELECTOR, f'[aria-label="{test_var}"]')

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    # 
    # Page Methods
    # 
    def load(self):
        self.browser.get(self._url)

    def get_title(self):
        title = self.browser.title
        return title

    def search(self, phrase):
        """
        An input method for Google's search field
        :param phrase: A search phrase (Untyped)
        """
        self.browser.find_element(*self._search_button)
        search_input = self.browser.find_element(*self._search_input)
        search_input.send_keys(phrase + Keys.RETURN)
