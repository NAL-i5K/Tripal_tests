# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
#from pyunitreport import HTMLTestRunner
#Chrome version 73.0.3683.86, ChromeDriver 73.0.3683.68
#Firefox version:58, Driver version:geckodriver24.0 
#IE version:11, IEDriverServer_x64_3.14.0
#Driver should put in the path of python3.6 or python2.7

class RegisterTestCase(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.get('https://i5k.nal.usda.gov/register/project-dataset/account')
        print('Test:https://i5k.nal.usda.gov/register/project-dataset/account')

    #namespace must be test....
    def test_register(self):
        driver=self.driver
        name_element = driver.find_element_by_xpath("//*[@id='edit-name']")
        name_element.send_keys("Test_Robot_production_register")
        print ('name_done')

        mail_element = driver.find_element_by_xpath("//*[@id='edit-email']")
        mail_element.send_keys("monica.poelchau@ars.usda.gov")
        print ('email_done')

        subject_element = driver.find_element_by_xpath("//*[@id='edit-affiliation']")
        subject_element.send_keys("Test_Robot_production_register")
        print ('Affiliation_done')

        message_element = driver.find_element_by_xpath("//*[@id='edit-content']")
        message_element.send_keys("Automated_Testing_for_production_register")
        print ('Contact_done')

        #Math question
        text=driver.find_element_by_xpath("//*[@id='project-dataset-submission-account']/div/div[6]/div").text
        question=str(text)
        number=[]
        print (text)
        for n in question.split():
            if n.isdigit():
                number.append(n)

        answer=int(number[0])+int(number[1])

        answer_field = driver.find_element_by_name("captcha_response")
        answer_field.send_keys(answer)
        print (answer)
        print ('Math_done')
        
        #click button
        submit_button = driver.find_element_by_xpath("//*[@id='edit-submit']")
        submit_button.click()

        #Get error message
        success_message=driver.find_element_by_xpath("/html/body/div[2]/div/section/div[1]").text
        print (success_message.encode('utf-8'))

    def tearDown(self):
        self.driver.quit()


class ContactTestCase(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.get('https://i5k.nal.usda.gov/contact')
        print('Test:https://i5k.nal.usda.gov/contact')

    #namespace must be test....
    def test_contact(self):
        driver=self.driver
        name_element = driver.find_element_by_xpath("//*[@id='edit-name']")
        name_element.send_keys("Test_Robot_production_contact")
        print ('name_done')

        mail_element = driver.find_element_by_xpath("//*[@id='edit-mail']")
        mail_element.send_keys("monica.poelchau@ars.usda.gov")
        print ('email_done')

        subject_element = driver.find_element_by_xpath("//*[@id='edit-subject']")
        subject_element.send_keys("Test_Robot_production_contact")
        print ('Subject_done')

        message_element = driver.find_element_by_xpath("//*[@id='edit-message']")
        message_element.send_keys("Automated_Testing_for_production_contact")
        print ('Message_done')

        #Math question
        text=driver.find_element_by_xpath("//*[@id='contact-site-form']/div/div[5]/div").text
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

        #click button
        submit_button = driver.find_element_by_xpath("//*[@id='edit-submit']")
        submit_button.click()
        
        #success message i5k:contact:"/html/body/div[2]/div/section/div[2]"
        success_message=driver.find_element_by_xpath("/html/body/div[2]/div/section/div[2]").text
        print (success_message.encode('utf-8'))

    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()


