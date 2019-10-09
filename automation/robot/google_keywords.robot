*** Settings ***
Library     Selenium2Library

*** Variables ***

${URL}              https://www.google.com
${BROWSER}          chrome
${SEARCH_PHRASE}    Pandaren

*** Keywords ***

Open Chrome
    Open Browser    ${URL}  ${BROWSER}

Close Chrome
    Close All Browsers

Verify Page Contains Google
    ${Get_title}=       Get Title
    Should Be Equal As Strings      ${Get_title}    Google

Search For A Phrase
    Press Keys      name:q      ${SEARCH_PHRASE}
    Press Keys      name:q      RETURN

Verify Links Appear
    ${count}=       Get Element Count   class:rc    
    Should Be True      ${count} > 0

Verify Search Input Contains Phrase
    Textfield Value Should Be      name:q      ${SEARCH_PHRASE}
