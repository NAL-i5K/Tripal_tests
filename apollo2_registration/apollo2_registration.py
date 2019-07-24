# -*- coding: utf-8 -*-
import argparse
import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import json
import requests

#from pyunitreport import HTMLTestRunner
#Chrome version 73.0.3683.86, ChromeDriver 73.0.3683.68
#Firefox version:58, Driver version:geckodriver24.0 
#IE version:11, IEDriverServer_x64_3.14.0
#Driver should put in the path of python3.6 or python2.7

class ApolloRegisterTestCase(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.get(args.url)
        print(args.url+'/web-apollo-registration')

    #namespace must be test....
    def test_register(self):
        driver=self.driver
        name_element = driver.find_element_by_xpath("//*[@id='edit-name']")
        name_element.send_keys("TEST BOT")
        print ('Full_name_done')

        mail_element = driver.find_element_by_xpath("//*[@id='edit-mail']")
        mail_element.send_keys("Chia-Tung.Wu@ars.usda.gov")
        print ('email_done')

        organism_element_select = driver.find_element_by_xpath("//*[@id='edit-organism']") 
        organism_element_select.send_keys("Varroa destructor")
        print ('organism_select_done')

        institution_element = driver.find_element_by_xpath("//*[@id='edit-institution']")
        institution_element.send_keys("NAL TEST")
        print ('Institution_done')

        comments_element = driver.find_element_by_xpath("//*[@id='edit-comments']")
        comments_element.send_keys("TEST")
        print ('Gene that you intend to annotate_done')

        #Math question
        text=driver.find_element_by_xpath("//*[@id='web-apollo-registration']/div/div[6]/div[1]/span").text
        question=str(text)
        number=[]
        print (text)
        for n in question.split():
            if n.isdigit():
                number.append(n)

        answer=int(number[0])+int(number[1])
        answer_field = driver.find_element_by_xpath("//*[@id='edit-captcha-response']")
        answer_field.send_keys(answer)
        print (answer)
        print ('Math_done')
        
        #click button
        submit_button = driver.find_element_by_xpath("//*[@id='edit-submit']")
        submit_button.click()
        print ('Button_click')
        
        #Get error message
        # error_message = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]").text
        # print (error_message.encode('utf-8'))
        # print ('----------------------------------------------------------------------')

        #Get success message
        success_message=driver.find_element_by_xpath("/html/body/div[2]/div/section/div[3]").text
        if success_message:
            print (success_message.encode('utf-8')+'...success')
        else:
            print ('failed')

        print ('----------------------------------------------------------------------')

    def tearDown(self):
        self.driver.quit()


class ApolloServerTestCase(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.get(args.url+'/user/login')
        print(args.url+'/user/login')

    #namespace must be test....
    def test_approval(self):
        driver=self.driver
        username_element = driver.find_element_by_xpath("//*[@id='edit-name']")
        username_element.send_keys("siteadmin")
        print ('username_done')

        password_element = driver.find_element_by_xpath("//*[@id='edit-pass']")
        password_element.send_keys("s1t3@admin")
        print ('email_done')

        #Math question
        text=driver.find_element_by_xpath("//*[@id='user-login']/div/div[3]/div").text
        print (text)
        question=str(text)
        number=[]

        for n in question.split():
            if n.isdigit():
                number.append(n)

        answer=int(number[0])+int(number[1])
        answer_field = driver.find_element_by_xpath("//*[@id='edit-captcha-response']")
        answer_field.send_keys(answer)
        print (answer)
        print ('Math_done')

        #Login button
        login_button = driver.find_element_by_xpath("//*[@id='edit-submit']")
        login_button.click()
        print ('Login_done')

        self.driver.get(args.url+'/admin/structure/webapollo/users2')
        edit_hyper = driver.find_elements_by_link_text('Edit')[0]
        edit_hyper.click()
        print ('redirect to siteadmin_page')
        
        #Radio button
        approve_button = driver.find_element_by_css_selector("input#edit-web-apollo2-table-status-1")
        approve_button.click()
        print ('Approve_done')

        #Save button
        save_button = driver.find_element_by_xpath("//*[@id='edit-web-apollo2-table-submit']")
        save_button.click()
        print ('Save_done')

        #Approve message
        approve_message = driver.find_element_by_xpath("//*[@id='content']/table[2]/tbody/tr[1]").text
        if approve_message:
            print (approve_message+'...success')
        else:
            print ('failed')        

        print ('----------------------------------------------------------------------')
    def tearDown(self):
        self.driver.quit()

#Check_databse
class ApolloVerificationTestCase(unittest.TestCase):
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
        print ('username_done')

        #Apollo_password
        password_element = driver.find_element_by_id("formPassword")
        password_element.send_keys("Newstand5Mesonic")
        print ('password_done')
        
        #Apollo_login
        login_button = driver.find_element_by_xpath("//*[@id='loginDialogId']/div/table/tbody/tr[2]/td[2]/div/form/fieldset/div[1]/div[6]/div[2]/button")
        login_button.click()
        print ('Apollo_login_done')
        driver.save_screenshot("screenshotapollo.png")
        driver.quit()

        #curl -i -X POST -H 'Content-Type: application/json' -d '{"username": "Chia-Tung.Wu@ars.usda.gov", "password": "Newstand5Mesonic", "name" : "Chia-Tung.Wu@ars.usda.gov"}' https://apollo.nal.usda.gov/apollo/user/loadUsers
        # headers = {
        # 'Content-Type': 'application/json',
        # }
        # data = '{"username": "i5k-user-admin@i5k.admin", "password": "i5k2user3admin", "name" : "Chia-Tung.Wu@ars.usda.gov"}'
        # response = requests.post('https://apollo.nal.usda.gov/apollo/user/loadUsers', headers=headers, data=data)
        # json = response.text
        # print (json)
        # if 'organismPermissions' in json:
        #     print ('Verification_done')

        #delete_user_api
        headers = {
        'Content-Type': 'application/json',
        }
        data = '{"username": "i5k-user-admin@i5k.admin", "password": "i5k2admin3password", "userToDelete": "Chia-Tung.Wu@ars.usda.gov"}'
        response = requests.post('https://apollo.nal.usda.gov/apollo/user/deleteUser', headers=headers, data=data)
        json= response.text
        print (json)

    def tearDown(self):
        self.driver.quit()

def get_parsed_args():
    parser=argparse.ArgumentParser()
    parser.add_argument('-u','--url', type=str, help='test_website')
    parser.add_argument('-a','--admin', type=str, help='username')
    parser.add_argument('-p','--password', type=str, help='password')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    get_parsed_args()
    unittest.main()
    #psql -c "delete from webapollo_users where email like '%Chia-Tung.Wu@ars.usda.gov%'"  -h gmod-stage-node1.nal.usda.gov -U postgres new_theme


