Feature: Google

    Background: 
        Given we are viewing the Google search page

    Scenario: Page Title Matches the Page
        Then the title should feature the Google name

    Scenario: Process a Google Search
        When we search for "Pandaren"
        Then "Pandaren" should appear in the results field