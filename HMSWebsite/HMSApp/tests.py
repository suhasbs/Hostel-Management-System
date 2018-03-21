# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.test import LiveServerTestCase
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# Create your tests here.

class LoginTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Firefox()
        self.selenium.implicitly_wait(2)
        super(LoginTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(LoginTestCase, self).tearDown()

    def test_case1(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/login/')
        #find the form element
        username = selenium.find_element_by_name('username')
        password = selenium.find_element_by_name('password')
        print "Testing for correct username and wrong password"
        submit = selenium.find_element_by_tag_name('button')
        
        username.send_keys('suhas')
        password.send_keys('suhas1234')
        submit.click()
        assert 'Wrong Login Credentials!' in selenium.page_source
        print "Test Case Passed\n\n"
        # username.send_keys('suhas')
        # password.send_keys('suhas123')
        # submit.send_keys(Keys.RETURN)
        # assert 'Wrong Login Credentials!' in selenium.page_source

    def test_case2(self):
        selenium = self.selenium
        #Opening the link we want to tests
        selenium.get('http://127.0.0.1:8000/login/')
        #find the form element
        username = selenium.find_element_by_name('username')
        password = selenium.find_element_by_name('password')
        print "Testing for wrong username and wrong password"
        submit = selenium.find_element_by_tag_name('button')
      
        username.send_keys('')
        password.send_keys('suhas1234')
        submit.click()
        # print selenium.page_source
        
        assert 'Wrong Login Credentials!' in selenium.page_source
        print "Test Case Passed\n\n"

    def test_case3(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/login/')
        #find the form element
        username = selenium.find_element_by_name('username')
        password = selenium.find_element_by_name('password')
        print "Testing for wrong username and correct password"
        submit = selenium.find_element_by_tag_name('button')
        
        username.send_keys('')
        password.send_keys('suhas123')
        submit.click()
        # print selenium.page_source
        
        assert 'Wrong Login Credentials!' in selenium.page_source
        print "Test Case Passed\n\n"

    def test_case4(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/login/')
        #find the form element
        username = selenium.find_element_by_name('username')
        password = selenium.find_element_by_name('password')
        print "Testing for correct username and correct password"
        submit = selenium.find_element_by_tag_name('button')
        
        username.send_keys('suhas')
        password.send_keys('suhas123')																										
        submit.click()
        # print selenium.page_source
        # time.sleep(10)
        # print selenium.page_source
        assert 'Dashboard' in selenium.page_source
        print "Test Case Passed\n\n"

# class LoginTestCase2(LiveServerTestCase):

#     def setUp(self):
#         self.selenium = webdriver.Firefox()
#         self.selenium.implicitly_wait(2)
#         super(LoginTestCase2, self).setUp()

#     def tearDown(self):
#         self.selenium.quit()
#         super(LoginTestCase2, self).tearDown()

#     def test_case2(self):
#         selenium = self.selenium
#         #Opening the link we want to tests
#         selenium.get('http://127.0.0.1:8000/login/')
#         #find the form element
#         username = selenium.find_element_by_name('username')
#         password = selenium.find_element_by_name('password')
#         print "Testing for wrong username and wrong password"
#         submit = selenium.find_element_by_tag_name('button')
      
#         username.send_keys('')
#         password.send_keys('suhas1234')
#         submit.click()
#         # print selenium.page_source
        
#         assert 'Wrong Login Credentials!' in selenium.page_source
#         print "Test Case Passed\n\n"

# class LoginTestCase3(LiveServerTestCase):

#     def setUp(self):
#         self.selenium = webdriver.Firefox()
#         self.selenium.implicitly_wait(2)
#         super(LoginTestCase3, self).setUp()

#     def tearDown(self):
#         self.selenium.quit()
#         super(LoginTestCase3, self).tearDown()

#     def test_case3(self):
#         selenium = self.selenium
#         #Opening the link we want to test
#         selenium.get('http://127.0.0.1:8000/login/')
#         #find the form element
#         username = selenium.find_element_by_name('username')
#         password = selenium.find_element_by_name('password')
#         print "Testing for wrong username and correct password"
#         submit = selenium.find_element_by_tag_name('button')
        
#         username.send_keys('')
#         password.send_keys('suhas123')
#         submit.click()
#         # print selenium.page_source
        
#         assert 'Wrong Login Credentials!' in selenium.page_source
#         print "Test Case Passed\n\n"


# class LoginTestCase4(LiveServerTestCase):

#     def setUp(self):
#         self.selenium = webdriver.Firefox()
#         self.selenium.implicitly_wait(2)
#         super(LoginTestCase4, self).setUp()

#     def tearDown(self):
#         # self.selenium.quit()
#         super(LoginTestCase4, self).tearDown()

#     def test_case4(self):
#         selenium = self.selenium
#         #Opening the link we want to test
#         selenium.get('http://127.0.0.1:8000/login/')
#         #find the form element
#         username = selenium.find_element_by_name('username')
#         password = selenium.find_element_by_name('password')
#         print "Testing for correct username and correct password"
#         submit = selenium.find_element_by_tag_name('button')
        
#         username.send_keys('suhas')
#         password.send_keys('suhas123')																										
#         submit.click()
#         # print selenium.page_source
#         # time.sleep(10)
#         # print selenium.page_source
#         assert 'Dashboard' in selenium.page_source
#         print "Test Case Passed\n\n"