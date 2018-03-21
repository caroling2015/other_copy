# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
import csv

class onestep(unittest.TestCase):
    # csv_reader = csv.reader(open('cc.csv'))
    # for each in csv_reader:
    #     account = each[0]
    #     password = each[1]

    def setUp(self):
        url = "http://127.0.0.1:81/zentao/user-login.html"
        # self.driver = webdriver.Ie()
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get(url)

        def test_login(self):
            username = self.driver.find_element_by_name("account")
            username.clear()
            username.send_keys("")
            password = self.driver.find_element_by_name("password")
            password.clear()
            password.send_keys("")
            submit = self.driver.find_element_by_id("submit")
            self.assertTrue(submit.is_enabled())
            submit.click()

        def tearDown(self):
            self.driver.quit()

if(__name__) == "__main__":
    unittest.main(verbosity=2)


