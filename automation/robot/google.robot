*** Settings ***
Resource        google_keywords.robot
Suite Setup     Open Chrome
Suite Teardown  Close Chrome

*** Test Cases ***

Open Google
    Verify Page Contains Google

Process A Google Search
    Search For A Phrase
    Verify Links Appear
    Verify Search Input Contains Phrase
