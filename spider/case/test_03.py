# coding:utf-8
import unittest

class TestThree(unittest.TestCase):

    def setUp(self):
        print('TestThree_setup!!!!')

    def testThree_01(self):
        print('TestThree测试用例01！！！')

    def testThreee_02(self):
        print('TestThree测试用例02！！！')

if __name__ =='__main__':
    unittest.main()
