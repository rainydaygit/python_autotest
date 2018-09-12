# coding:utf-8
import unittest
from common.re_token import get_token

class Test_02(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.token = get_token()
        print("获取到当前用例token值：%s" % cls.token)

    def test_03(self):
        '''测试用例1'''
        body1 = {
            "a": "111111",
            "b": "111111",
            "token": self.token  # 参数关联
        }
        print("用例1body：%s" % body1)

    def test_04(self):
        '''测试用例2'''
        body1 = {
            "a": "222222",
            "b": "2222222",
            "token": self.token  # 参数关联
        }
        print("用例1body：%s" % body1)

if __name__ == "__main__":
    unittest.main()