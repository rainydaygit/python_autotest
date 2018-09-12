# -*- coding:utf-8 -*-

import unittest
import requests
import json
import urllib3

class RunMain(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        print('这是初始化------')

    def tearDown(self):
        print('这是清理--------')

    def test_login(self):
        print('这是测试用例login')

    def test_exit(self):
        print('这是测试用例exit')

if __name__ == '__main__':
    unittest.main()