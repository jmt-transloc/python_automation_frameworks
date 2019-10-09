from behave import *

@when('we navigate to the Google homepage')
def step(context):
    context.browser.get('https://www.google.com')

@then('the title should feature the Google name')
def step(context):
    assert context.browser.title == 'Google'
