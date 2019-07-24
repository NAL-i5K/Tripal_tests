*** Settings ***
Resource          resource.txt
Library     BuiltIn
Library     String
*** Variables ***
${url}
${username}
${password}
*** Test Cases ***
ApolloRegisterTestCase
    Open Browser  ${url}/web-apollo-registration  headlesschrome
    Wait and Input  xpath=//*[@id='edit-name']  TEST BOT
    Wait and Input  xpath=//*[@id='edit-mail']  Chia-Tung.Wu@ars.usda.gov
    click element   xpath=//*[@id="edit-organism"]/option[52]
    Wait and Input  xpath=//*[@id='edit-institution']  NAL TEST
    Wait and Input  xpath=//*[@id='edit-comments']  TEST
    #Wait and Input  xpath=//*[@id='edit-captcha-response']
    #CLick Element   //*[@id='edit-submit']
    ${my_string}  Get Text  xpath=//*[@id='web-apollo-registration']/div/div[6]/div[1]/span  
    @{MyList}=  Create List    
    Math  MyList  my_string
    log ${Mathresult}
    [Teardown]    Close All Browsers

ApolloServerTestCase
    # Open Browser  ${url}/user/login  headlesschrome
    # Wait and Input  xpath=//*[@id='edit-name']  siteadmin
    # Wait and Input  xpath=//*[@id='edit-pass']  s1t3@admin
#     Wait and Input  xpath=//*[@id='edit-submit']  click
    [Teardown]    Close All Browsers

*** Keywords ***
Wait and Input 
    [Arguments]  ${locator}  ${text}
    Wait Until Element is Visible  ${locator}
    Input Text  ${locator}  ${text}
Math 
    [Arguments]  ${list}  ${string}
    :FOR  ${number}  IN  Split String  ${string}
    \ Run Keyword If ${number} isdigit()
    \ Append To List  ${list} ${number}
    ${Mathresult} = Evaluate  @{list}[0]+@{list}[1]


