*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
Registration Testing
    Open Browser  https://gmod-stage.nal.usda.gov/register/project-dataset/account  headlesschrome
    Wait and Input  name=name  Test_Robot
    Wait and Input  xpath=//*[@id='edit-email']  monica.poelchau@ars.usda.gov
    Wait and Input  name=affiliation  Test_Robot
    Wait and Input  name=content  Automated Testing
    [Teardown]    Close All Browsers

Contact Testing
    Open Browser  https://gmod-stage.nal.usda.gov/contact  headlesschrome
    Wait and Input  name=name  Test_Robot
    Wait and Input  xpath=//*[@id='edit-mail']  monica.poelchau@ars.usda.gov
    Wait and Input  xpath=//*[@id='edit-subject']  Test_Robot
    Wait and Input  xpath=//*[@id='edit-message']  Automated Testing
    [Teardown]    Close All Browsers

*** Keywords ***
Wait and Input 
    [Arguments]  ${locator}  ${text}
    Wait Until Element is Visible  ${locator}
    Input Text  ${locator}  ${text}

