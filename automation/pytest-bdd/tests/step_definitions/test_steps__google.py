from pytest_bdd import scenarios, given, when, then, parsers
from pages.search import GoogleSearch
from pages.results import GoogleResults

#
# Scenarios
#
scenarios('../features/google.feature')


#
# Background:
#
@given('we are viewing the Google search page')
def navigate_to_page(browser):
    search_page = GoogleSearch(browser)
    search_page.load()


#
# Test: Page Title Matches the Page
#
@then('the title should feature the Google name')
def compare_title(browser):
    search_page = GoogleSearch(browser)
    assert search_page.get_title() == 'Google'


#
# Test: Process a Google Search
#
@when(parsers.parse('we search for "{phrase}"'))
def search(browser, phrase):
    search_page = GoogleSearch(browser)
    search_page.search(phrase)


@then(parsers.parse('"{phrase}" should appear in the results field'))
def verify_search_results(browser, phrase):
    results_page = GoogleResults(browser)
    assert results_page.result_div_count() > 0
    assert results_page.search_input_value(results_page.search_field) == phrase
