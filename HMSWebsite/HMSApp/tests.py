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

    def test_register(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/login/')
        #find the form element
        username = selenium.find_element_by_name('username')
        password = selenium.find_element_by_name('password')
        print username, password
        submit = selenium.find_element_by_tag_name('button')
        print submit
        username.send_keys('suhas')
        password.send_keys('suhas1234')
        submit.send_keys(Keys.RETURN)
        # print selenium.page_source
        time.sleep(1)
        assert 'Wrong Login Credentials!' in selenium.page_source

        # username.send_keys('suhas')
        # password.send_keys('suhas123')
        # submit.send_keys(Keys.RETURN)
        # assert 'Wrong Login Credentials!' in selenium.page_source

class LoginTestCase2(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Firefox()
        self.selenium.implicitly_wait(2)
        super(LoginTestCase2, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(LoginTestCase2, self).tearDown()

    def test_register(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/login/')
        #find the form element
        username = selenium.find_element_by_name('username')
        password = selenium.find_element_by_name('password')
        print username, password
        submit = selenium.find_element_by_tag_name('button')
        print submit
        username.send_keys('')
        password.send_keys('suhas1234')
        submit.send_keys(Keys.RETURN)
        # print selenium.page_source
        time.sleep(1)
        assert 'Wrong Login Credentials!' in selenium.page_source

class LoginTestCase3(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Firefox()
        self.selenium.implicitly_wait(2)
        super(LoginTestCase3, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(LoginTestCase3, self).tearDown()

    def test_register(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/login/')
        #find the form element
        username = selenium.find_element_by_name('username')
        password = selenium.find_element_by_name('password')
        print username, password
        submit = selenium.find_element_by_tag_name('button')
        print submit
        username.send_keys('')
        password.send_keys('suhas123')
        submit.send_keys(Keys.RETURN)
        # print selenium.page_source
        time.sleep(1)
        assert 'Wrong Login Credentials!' in selenium.page_source


class LoginTestCase4(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Firefox()
        self.selenium.implicitly_wait(2)
        super(LoginTestCase4, self).setUp()

    def tearDown(self):
        # self.selenium.quit()
        super(LoginTestCase4, self).tearDown()

    def test_register(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/login/')
        #find the form element
        username = selenium.find_element_by_name('username')
        password = selenium.find_element_by_name('password')
        print username, password
        submit = selenium.find_element_by_tag_name('button')
        print submit
        username.send_keys('suhas')
        password.send_keys('suhas123')
        submit.send_keys(Keys.RETURN)
        # print selenium.page_source
        time.sleep(10)
        print selenium.page_source
        assert 'Dashboard' in selenium.page_source