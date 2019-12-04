from tests.pages.search import GoogleSearchPage
from tests.pages.results import GoogleResultsPage


def test_refactored_browser_search(browser):
    """ Test search functionality """
    phrase = 'Pandaren'

    search_page = GoogleSearchPage(browser)
    search_page.load()
    search_page.search(phrase)

    results_page = GoogleResultsPage(browser)
    assert results_page.result_div_count() > 0
    assert results_page.search_input_value(results_page.search_field()) == phrase
