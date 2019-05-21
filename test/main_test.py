#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
import main


class MyTestCase(unittest.TestCase):

    def setUp(self):
        # 每个测试用例执行之前做操作
        pass

    def test_something(self):
        a = 1
        b = 2
        c, d = main.class_a.func(a, b)
        self.assertEqual(c, 2)
        self.assertEqual(d, 1)

    def tearDown(self):
        # 每个测试用例执行之后做操作
        pass


if __name__ == '__main__':
    unittest.main()
