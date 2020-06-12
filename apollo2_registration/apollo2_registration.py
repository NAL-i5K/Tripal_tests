# -*- coding: utf-8 -*-
import os
#import sys
import unittest
from selenium import webdriver
#import time
#from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.support.ui import Select
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support.wait import WebDriverWait
#import json
#import requests
import psycopg2

#from pyunitreport import HTMLTestRunner
#Chrome version 73.0.3683.86, ChromeDriver 73.0.3683.68
#Firefox version:58, Driver version:geckodriver24.0
#IE version:11, IEDriverServer_x64_3.14.0
#Driver should put in the path of python3.6 or python2.7

class ApolloRegisterTestCase(unittest.TestCase):
    #Declaration
    DBUSER = "dbuser"
    TESTURL = "testurl"
    DBHOST = "dbhost"
    TESTDB = "testdb"
    DBPW = "dbpw"

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.get(self.TESTURL)
        print((self.TESTURL))

    #namespace must be test....
    def test_register(self):
        #Initialize-clear-table(testmail)
        connection=psycopg2.connect(host=self.DBHOST, user=self.DBUSER, password=self.DBPW, dbname=self.TESTDB)
        cur=connection.cursor()
        cur.execute("delete from webapollo_users where email like '%Chia-Tung.Wu@ars.usda.gov%'")
        print((cur.statusmessage))
        print('Initialize')
        connection.commit()
        connection.close()
        driver=self.driver
        name_element = driver.find_element_by_xpath("//*[@id='edit-name']")
        name_element.send_keys("TEST BOT")
        print('Full_name_done')

        mail_element = driver.find_element_by_xpath("//*[@id='edit-mail']")
        mail_element.send_keys("Chia-Tung.Wu@ars.usda.gov")
        print('email_done')

        organism_element_select = driver.find_element_by_xpath("//*[@id='edit-organism']")
        organism_element_select.send_keys("Varroa destructor")
        print('organism_select_done')

        institution_element = driver.find_element_by_xpath("//*[@id='edit-institution']")
        institution_element.send_keys("NAL TEST")
        print('Institution_done')

        comments_element = driver.find_element_by_xpath("//*[@id='edit-comments']")
        comments_element.send_keys("TEST")
        print('Gene that you intend to annotate_done')

        #Math question
        text=driver.find_element_by_xpath("//*[@id='web-apollo-registration']/div/fieldset/div/div[2]/span").text
        question=str(text)
        number=[]
        print(text)
        for n in question.split():
            if n.isdigit():
                number.append(n)

        answer=int(number[0])+int(number[1])
        answer_field = driver.find_element_by_xpath("//*[@id='edit-captcha-response']")
        answer_field.send_keys(answer)
        print(answer)
        print('Math_done')

        #click button
        submit_button = driver.find_element_by_xpath("//*[@id='edit-submit']")
        submit_button.click()
        print('Button_click')

        #Get success message
        success_message=driver.find_element_by_xpath("/html/body/div[2]/div/section/div[3]").text
        if success_message:
            print((success_message.encode('utf-8')+'...success'))
        else:
            exit()

        print('----------------------------------------------------------------------')

    def tearDown(self):
        self.driver.quit()


class ApolloServerTestCase(unittest.TestCase):
    LOGIN="GmodURL"
    APPROVE="GmodApprove"
    SITEUSER="GmodSiteUser"
    SITEPASS="GmodSitePassword"

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.get(self.LOGIN)
        print((self.LOGIN))

    #namespace must be test....
    def test_approval(self):
        driver=self.driver
        username_element = driver.find_element_by_xpath("//*[@id='edit-name']")
        username_element.send_keys(self.SITEUSER)
        print('username_done')

        password_element = driver.find_element_by_xpath("//*[@id='edit-pass']")
        password_element.send_keys(self.SITEPASS)
        print('password_done')

        #Math question
        text=driver.find_element_by_xpath("//*[@id='user-login']/div/fieldset/div/div[2]").text
        print(text)
        question=str(text)
        number=[]

        for n in question.split():
            if n.isdigit():
                number.append(n)

        answer=int(number[0])+int(number[1])
        answer_field = driver.find_element_by_xpath("//*[@id='edit-captcha-response']")
        answer_field.send_keys(answer)
        print(answer)
        print('Math_done')

        #Login button
        login_button = driver.find_element_by_xpath("//*[@id='edit-submit']")
        login_button.click()
        print('Login_done')

        #Move to approve page
        self.driver.get(self.APPROVE)
        edit_hyper = driver.find_elements_by_link_text('Edit')[0]
        edit_hyper.click()
        print('redirect to siteadmin_page')

        #Radio button
        approve_button = driver.find_element_by_css_selector("input#edit-web-apollo2-table-status-1")
        approve_button.click()
        print('Approve_done')

        #Save button
        save_button = driver.find_element_by_xpath("//*[@id='edit-web-apollo2-table-submit']")
        save_button.click()
        print('Save_done')

        #Approve message
        approve_message = driver.find_element_by_xpath("//*[@id='content']/table[2]/tbody/tr[1]").text
        if approve_message:
            print((approve_message +'...success'))
        else:
            exit()

        print('----------------------------------------------------------------------')
    def tearDown(self):
        self.driver.quit()

#Check_database
class ApolloVerificationTestCase(unittest.TestCase):
    DBUSER = "Tony"
    DBHOST = "i5khost"
    TESTDB = "i5kdb"
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.maximize_window()
        self.driver.get('http://apollo.nal.usda.gov/apollo')
        print('Test:http://apollo.nal.usda.gov/apollo')

    #namespace must be test....
    def test_Verification(self):
        driver=self.driver
        driver.implicitly_wait(10)
        username_element = driver.find_element_by_xpath("//*[@id='formName']")
        username_element.send_keys("Chia-Tung.Wu@ars.usda.gov")
        print('username_done')

        #Apollo_password
        password_element = driver.find_element_by_id("formPassword")
        password_element.send_keys("Newstand5Mesonic")
        print('password_done')

        #Apollo_login
        login_button = driver.find_element_by_xpath("//*[@id='loginDialogId']/div/table/tbody/tr[2]/td[2]/div/form/fieldset/div[1]/div[6]/div[2]/button")
        login_button.click()
        print('Apollo_login_done')
        driver.save_screenshot("screenshotapollo.png")
        driver.quit()

        #check_user
        connection=psycopg2.connect(host=self.DBHOST, user=self.DBUSER, dbname=self.TESTDB)
        cur=connection.cursor()
        cur.execute("select * from webapollo_users where email like '%Chia-Tung.Wu@ars.usda.gov%'")
        row=cur.fetchall()
        if row:
            print(row)
        else:
            print('Cannot find user in webapollo_users')
            exit()
        #delete_user_from_table
        cur.execute("delete from webapollo_users where email like '%Chia-Tung.Wu@ars.usda.gov%'")
        print((cur.statusmessage))
        connection.commit()
        connection.close()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    #get variables
    ApolloRegisterTestCase.DBUSER = os.environ.get('DBUSER', ApolloRegisterTestCase.DBUSER)
    ApolloRegisterTestCase.DBHOST = os.environ.get('DBHOST', ApolloRegisterTestCase.DBHOST)
    ApolloRegisterTestCase.TESTDB = os.environ.get('TESTDB', ApolloRegisterTestCase.TESTDB)
    ApolloRegisterTestCase.TESTURL = os.environ.get('TESTURL', ApolloRegisterTestCase.TESTURL)

    ApolloServerTestCase.LOGIN = os.environ.get('LOGIN', ApolloServerTestCase.LOGIN)
    ApolloServerTestCase.APPROVE = os.environ.get('APPROVE', ApolloServerTestCase.APPROVE)
    ApolloServerTestCase.SITEUSER = os.environ.get('SITEUSER', ApolloServerTestCase.SITEUSER)
    ApolloServerTestCase.SITEPASS = os.environ.get('SITEPASS', ApolloServerTestCase.SITEPASS)

    ApolloVerificationTestCase.DBUSER = os.environ.get('DBUSER', ApolloVerificationTestCase.DBUSER)
    ApolloVerificationTestCase.DBHOST = os.environ.get('DBHOST', ApolloVerificationTestCase.DBHOST)
    ApolloVerificationTestCase.TESTDB = os.environ.get('TESTDB', ApolloVerificationTestCase.TESTDB)

    unittest.main()

