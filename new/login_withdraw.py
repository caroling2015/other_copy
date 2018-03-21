# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver

class login(unittest.TestCase):
    def setUp(self):
        url = "http://old.rightbtc.net/#!/login"
        # self.driver = webdriver.Ie()
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(url)

    def test_login(self):
        username = self.driver.find_element_by_xpath("//input[@name='username']")
        username.clear()
        username.send_keys("tester_tt01@163.com")
        password = self.driver.find_element_by_xpath("//input[@name='passward']")
        password.clear()
        password.send_keys("1357asdf")
        submit = self.driver.find_element_by_xpath("//button[@type='submit']")
        self.assertTrue(submit.is_enabled())
        submit.click()

    def tearDown(self):
        self.driver.quit()

if(__name__) == "__main__":
    unittest.main(verbosity=2)

