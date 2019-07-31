# -*- coding: utf-8 -*-
import os
import sys
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
import psycopg2

#from pyunitreport import HTMLTestRunner
#Chrome version 73.0.3683.86, ChromeDriver 73.0.3683.68
#Firefox version:58, Driver version:geckodriver24.0 
#IE version:11, IEDriverServer_x64_3.14.0
#Driver should put in the path of python3.6 or python2.7

class RequestTestCase(unittest.TestCase):
    #Declaration  
    TESTURL = "i5kurl"
    SITEUSER="GmodSiteUser"
    SITEPASS="GmodSitePassword"

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        #https://gmod-stage.nal.usda.gov/user/login?destination=datasets/request-project
        self.driver.get(self.TESTURL)
        print(self.TESTURL)

    #namespace must be test....
    def test_request(self):
        #Initialize-clear-table(testmail)
        # connection=psycopg2.connect(host=self.DBHOST, user=self.DBUSER, dbname=self.TESTDB)
        # cur=connection.cursor()
        # cur.execute("delete from webapollo_users where email like '%Chia-Tung.Wu@ars.usda.gov%'")
        # print (cur.statusmessage)
        # print ('Initialize')
        # connection.commit()
        # connection.close()

        #new request login
        driver=self.driver
        username_element = driver.find_element_by_xpath("//*[@id='edit-name']")
        username_element.send_keys(self.SITEUSER)
        print ('username_done')

        password_element = driver.find_element_by_xpath("//*[@id='edit-pass']")
        password_element.send_keys(self.SITEPASS)
        print ('password_done')
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

        #Move to Request Page
        genus_element = driver.find_element_by_xpath("//*[@id='edit-genus']")
        genus_element.send_keys("TEST GENUS")
        print ('genus_done')

        species_element = driver.find_element_by_xpath("//*[@id='edit-species']")
        species_element.send_keys("TEST SPECIES")
        print ('species_done')

        taxid_element = driver.find_element_by_xpath("//*[@id='edit-ncbi-taxid']")
        taxid_element.send_keys("101010")
        print ('taxid_done')

        common_element = driver.find_element_by_xpath("//*[@id='edit-common-name']")
        common_element.send_keys("TEST COMMON")
        print ('common_done')

        dataset_element = driver.find_element_by_xpath("//*[@id='edit-is-genome-assembly']")
        dataset_element.send_keys("TEST DATASET")
        print ('dataset_done')

        ncbimember_element_select = driver.find_element_by_xpath("//*[@id='edit-is-ncbi-submitted']") 
        ncbimember_element_select.send_keys("Yes")
        print ('ncbimember_done')

        reassembly_element_select = driver.find_element_by_xpath("//*[@id='edit-is-assembly']") 
        reassembly_element_select.send_keys("Yes")
        print ('reassembly_done')

        involved_element_select = driver.find_element_by_xpath("//*[@id='edit-involved-in-generation']") 
        involved_element_select.send_keys("Yes")
        print ('involved_done')

        description_element = driver.find_element_by_xpath("//*[@id='edit-description']")
        description_element.send_keys("TEST DESCRIPTION")
        print ('description_done')

        fullname_element = driver.find_element_by_xpath("//*[@id='edit-fullname']")
        fullname_element.send_keys("TEST FULLNAME")
        print ('fullname_done')

        email_element = driver.find_element_by_xpath("//*[@id='edit-email']")
        email_element.send_keys("Chia-Tung.Wu@ars.usda.gov")
        print ('email_done')

        #click button
        submit_button = driver.find_element_by_xpath("//*[@id='edit-submit']")
        submit_button.click()
        print ('Button_click')

    def tearDown(self):
        self.driver.quit()

#Check_database
class TestDatabaseTestCase(unittest.TestCase):
    DBUSER = "Tony"
    DBHOST = "i5khost"
    TESTDB = "i5kdb"
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        # self.driver.maximize_window()
        # self.driver.get('http://apollo.nal.usda.gov/apollo')
        print('Test:'+self.DBHOST)

    #namespace must be test....
    def test_TestDatabase(self):
        #check_user
        connection=psycopg2.connect(host=self.DBHOST, user=self.DBUSER, dbname=self.TESTDB)
        cur=connection.cursor()
        #cur.execute("select * from webapollo_users where email like '%Chia-Tung.Wu@ars.usda.gov%'")
        cur.execute("select * from ds_request_project where email like '%Chia-Tung.Wu@ars.usda.gov%'")
        row=cur.fetchall()
        if row:
            print (row)
        else:
            print ('Cannot find user in webapollo_users')
            exit()
        #delete_user_from_table
        #cur.execute("delete from webapollo_users where email like '%Chia-Tung.Wu@ars.usda.gov%'")
        #print (cur.statusmessage)
        connection.commit()
        connection.close()

    def tearDown(self):
        self.driver.quit()

class TestDrupalApprovalTestCase(unittest.TestCase):
    LOGIN="GmodLogin"
    APPROVE="GmodApprove"
    SITEUSER="GmodSiteUser"
    SITEPASS="GmodSitePassword"

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.get('https://gmod-stage.nal.usda.gov/user/login')

    #namespace must be test....
    def test_approval(self):
        driver=self.driver
        username_element = driver.find_element_by_xpath("//*[@id='edit-name']")
        username_element.send_keys(self.SITEUSER)
        print ('username_done')

        password_element = driver.find_element_by_xpath("//*[@id='edit-pass']")
        password_element.send_keys(self.SITEPASS)
        print ('password_done')

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

        #Move to approve page
        self.driver.get(self.APPROVE)
        edit_hyper = driver.find_elements_by_link_text('Edit')[0]
        edit_hyper.click()
        print ('redirect to siteadmin_page')
        
        approve_button = driver.find_element_by_css_selector("input#edit-datasets-table-status-1")
        approve_button.click()
        print ('Approve_done')

        #Save button 
        save_button = driver.find_element_by_xpath("//*[@id='edit-datasets-table-submit']")
        save_button.click()
        print ('Save_done')

        #submit a dataset
        self.driver.get('https://gmod-stage.nal.usda.gov/datasets/submit-a-dataset')
        
        organism_element_select = driver.find_element_by_xpath("//*[@id='edit-organism']") 
        organism_element_select.send_keys("Varroa destructor")
        print ('organism_done')

        dateset_element = driver.find_element_by_xpath("//*[@id='edit-dataset-name']")
        dateset_element.send_keys("Test_dateset")
        print ('dateset_done')

        program_element = driver.find_element_by_xpath("//*[@id='edit-program']")
        program_element.send_keys("Test_program")
        print ('program_done')

        dateset_element = driver.find_element_by_xpath("//*[@id='edit-dataset-version']")
        dateset_element.send_keys("10.0.0")
        print ('dataset_version_done')

        dateset_element = driver.find_element_by_xpath("//*[@id='edit-version']")
        dateset_element.send_keys("10.0.0")
        print ('program_version_done')

        #selector edit-is-download
        download_element_select = driver.find_element_by_xpath("//*[@id='edit-is-download']") 
        download_element_select.send_keys("No")
        print ('download_done')

        #selector edit-dataset-is-publish
        publish_element_select = driver.find_element_by_xpath("//*[@id='edit-dataset-is-publish']") 
        publish_element_select.send_keys("No")
        print ('publish_done')

        genome_assembly_element = driver.find_element_by_xpath("//*[@id='edit-assembly']/legend/a")
        genome_assembly_element.click()
        print ('genome_assembly_done')

        sha_element = driver.find_element_by_xpath("//*[@id='edit-sha512']")
        sha_element.send_keys("0123456789")
        print ('sha_done')

        url_element = driver.find_element_by_xpath("//*[@id='edit-sha512']")
        url_element.send_keys("https://gmod-stage.nal.usda.gov")
        print ('url_done')

        toronto_element = driver.find_element_by_xpath("//*[@id='edit-dataset-publish-field-data']") 
        toronto_element.send_keys("No")
        print ('toronto_done')

        #Genome assembly information

        background_element = driver.find_element_by_xpath("//*[@id='edit-description']") 
        background_element.send_keys("Test_background")
        print ('background_done')
        
        image_element= driver.find_element_by_xpath("//*[@id='edit-organism-image-filename']") 
        image_element.send_keys("Test_image")
        print ('image_done')

        curate_element_select= driver.find_element_by_xpath("//*[@id='edit-is-curate-assembly']") 
        curate_element_select.send_keys("No")
        print ('curate_done')

        geographic_element= driver.find_element_by_xpath("//*[@id='edit-assembly-geo-location']") 
        geographic_element.send_keys("Test_geographic")
        print ('geographic_done')

        tissues_element= driver.find_element_by_xpath("//*[@id='edit-assembly-tissues-located']") 
        tissues_element.send_keys("Test_tissues")
        print ('tissues_done')

        #edit-assembly-gender
        gender_element_select = driver.find_element_by_xpath("//*[@id='edit-assembly-gender']") 
        gender_element_select.send_keys("Male")
        print ('gender_done')

        strain_element= driver.find_element_by_xpath("//*[@id='edit-data-source-strain']") 
        strain_element.send_keys("Test_strain")
        print ('strain_done')

        notes_element= driver.find_element_by_xpath("//*[@id='edit-data-source-notes']") 
        notes_element.send_keys("Test_notes")
        print ('notes_done')

        seqplatform_element= driver.find_element_by_xpath("//*[@id='edit-data-source-seqplatform']") 
        seqplatform_element.send_keys("Test_seqplatform")
        print ('seqplatforms_done')

        accession_element= driver.find_element_by_xpath("//*[@id='edit-assembly-accession']") 
        accession_element.send_keys("Test_accession")
        print ('accession_done')

        othernote_element= driver.find_element_by_xpath("//*[@id='edit-additional-other-notes']") 
        othernote_element.send_keys("Test_othernote")
        print ('othernote_done')

        #Genome set information
        #Mapped dataset

        # success_message = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]").text
        # if success_message:
        #     print (success_message+'...success')
        # else:
        #     exit()        

        # print ('----------------------------------------------------------------------')
    def tearDown(self):
        self.driver.quit()
    
if __name__ == '__main__':  
    #get variables
    RequestTestCase.TESTURL = os.environ.get('TESTURL', RequestTestCase.TESTURL) 
    RequestTestCase.SITEUSER = os.environ.get('SITEUSER', RequestTestCase.SITEUSER)
    RequestTestCase.SITEPASS = os.environ.get('SITEPASS', RequestTestCase.SITEPASS) 
    
    TestDatabaseTestCase.DBHOST = os.environ.get('DBHOST', TestDatabaseTestCase.DBHOST)
    TestDatabaseTestCase.TESTDB = os.environ.get('TESTDB', TestDatabaseTestCase.TESTDB)
    TestDatabaseTestCase.DBUSER = os.environ.get('DBUSER', TestDatabaseTestCase.DBUSER)

    # TestDrupalApprovalTestCase.LOGIN = os.environ.get('LOGIN', TestDrupalApprovalTestCase.LOGIN)
    TestDrupalApprovalTestCase.APPROVE = os.environ.get('APPROVE', TestDrupalApprovalTestCase.APPROVE)
    TestDrupalApprovalTestCase.SITEUSER = os.environ.get('SITEUSER', TestDrupalApprovalTestCase.SITEUSER)
    TestDrupalApprovalTestCase.SITEPASS = os.environ.get('SITEPASS', TestDrupalApprovalTestCase.SITEPASS) 


    # ApolloVerificationTestCase.DBUSER = os.environ.get('DBUSER', ApolloVerificationTestCase.DBUSER) 
    # ApolloVerificationTestCase.DBHOST = os.environ.get('DBHOST', ApolloVerificationTestCase.DBHOST)
    # ApolloVerificationTestCase.TESTDB = os.environ.get('TESTDB', ApolloVerificationTestCase.TESTDB)

    unittest.main()

