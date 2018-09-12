# coding:utf-8
import unittest

class TestTwo(unittest.TestCase):

    def setUp(self):
        print('TestTwo_setup!!!!')

    def testTwo_01(self):
        print('TestTwo测试用例01！！！')

    def testTwo_02(self):
        print('TestTwo测试用例02！！！')

if __name__ =='__main__':
    unittest.main()