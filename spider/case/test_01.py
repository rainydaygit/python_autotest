# coding:utf-8
import unittest
from selenium import webdriver
from common.logger import Log

class TestOne(unittest.TestCase):

    def setUp(self):
        self.log = Log()
        print('TestOne_setup!!!!')

    def testOne_01(self):
        u'''TestOne测试用例01！！！'''
        # browser = webdriver.Chrome()
        # browser.get('https://www.baidu.com/')
        self.assertEquals(1, 2)
        self.log.info('测试用例01')
        #browser.quit()


    def testOne_02(self):
        u'''TestOne测试用例02！！！'''
        self.assertEquals(2, 2)
        self.log.info('测试用例02')

if __name__ =='__main__':
    unittest.main()