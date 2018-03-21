# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import csv
import time

class login(unittest.TestCase):
    url = "http://old.rightbtc.net/"

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get(self.url + '#!/login')

    def login(self,name,pwd):
        username = self.driver.find_element_by_xpath("//input[@name='username']")
        username.clear()
        username.send_keys(name)
        password = self.driver.find_element_by_xpath("//input[@name='passward']")
        password.clear()
        password.send_keys(pwd)
        submit = self.driver.find_element_by_xpath("//button[@type='submit']")
        if submit.is_enabled():
            submit.click()
        else:
            print "用户名或密码格式不正确"
        # self.assertTrue(submit.is_enabled())


    def is_login_suc(self,name):
        u'''判断是否获取到登录账户名称'''
        try:
            jugename = name[:2] + "********" + name[-7:]
            #字符串取前三，后七位，中间用8个*号取代
            text = self.driver.find_element_by_tag_name(jugename)#待判断是否执行成功
            return True
        except:
            return False

    def test_login_i(self):
        csv_reader = csv.reader(open('cc.csv'))
        i = 1
        for row in csv_reader:
            print row
            print "第%d条开始。。" % i
            self.login(row[0], row[1])
            time.sleep(3)
            if self.is_login_suc(row[0])=="False":
                return
            else:
                print "第%d条执行成功。。" % i
                # self.driver.get("http://old.rightbtc.net/#!/setting/menu")
                self.driver.get(self.url + '#!/logout')
                time.sleep(3)
                print "第%d条结束。。" % i
            i = i + 1

    def test_withdraw(self):
        self.driver.get(self.url + '#!/account/withdraw')



    def tearDown(self):
        self.driver.quit()

if(__name__) == "__main__":
    unittest.main(verbosity=2)

