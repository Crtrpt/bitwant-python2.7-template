#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
import time
import main
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC  # available since 2.26.0


class MyTestCase(unittest.TestCase):

    def setUp(self):
        # 每个测试用例执行之前做操作
        print(u"运行之前")

    def test_something(self):
        a = 1
        b = 2
        c, d = main.class_a.func(a, b)
        self.assertEqual(c, 2)
        self.assertEqual(d, 1)
        # driver = webdriver.Chrome()
        # driver.get("http://39.100.73.189")
        # e = driver.find_element_by_css_selector('body > div > div.content > div.title.m-b-md')
        # self.assertEqual(e.text, u"比特刀锋")
        # time.sleep(10)

    def tearDown(self):
        # 每个测试用例执行之后做操作
        print(u"运行之后")


if __name__ == '__main__':
    unittest.main()
