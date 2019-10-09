# test_web
import pytest

from pages.search import GoogleSearchPage
from pages.results import GoogleResultsPage

def test_refactored_browser_search(browser):
    PHRASE = 'Pandaren'
    
    search_page = GoogleSearchPage(browser)
    search_page.load()
    search_page.search(PHRASE)

    results_page = GoogleResultsPage(browser)
    assert results_page.result_div_count() > 0
    assert results_page.search_input_value() == PHRASE
