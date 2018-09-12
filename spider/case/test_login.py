# coding:utf-8
import requests
import unittest
import re
import json
import time
import urllib3
from config import read_config, read_yaml
from common import mock_server

urllib3.disable_warnings()
ti = int(time.time())
class TestLogin(unittest.TestCase):

    def setUp(self):
        self.token = read_yaml.get_token()[0]
        self.cookies1 = {
            'Cookie': 'JSESSIONID=' + read_yaml.get_token()[1]
        }

    @unittest.skip('test_hand_pwd_login')
    def test_hand_pwd_login(self):

        # print(self.cookies1)
        url = read_config.get_user_info('url') + '/emm-api/handPwdLogin.json'
        # print(url)
        body = {
                'loginname': read_config.get_user_info('loginname'),
                'uidmobiledevid': '869897034335694',
                'iostype': '2',
                'strhandpwd': '1235789',
                'handpwdtimestamp': ti,
                'devicetype': 'android_phone',
                'clientversion': '2.3.8'
        }
        res = requests.post(url, data=body, headers=self.cookies1, verify=False)
        # print(res.headers)
        # print(res.text)
        res_status = res.json()['status']
        # try:
        #     res = int(re.findall(r'"status":(.+\d?)', res.text)[0])
        # except:
        #     print('接口异常，返回数据: '+res.text)
        self.assertEqual(res_status, 2000, msg=res.text)

    @unittest.skip('test_registinfo_service')
    def test_registinfo_service(self):
        # print(self.cookies1)
        url = read_config.get_user_info('url') + '/emm-api/information/registInfoService.json'
        # print(url)
        body = {
                'loginname': read_config.get_user_info('loginname'),
                'uidmobiledevid': read_config.get_user_info('uidmobiledevid'),
                'tokenid': self.token,
                'devicetype': 'android_phone',
                'devicetoken': read_config.get_user_info('uidmobiledevid')
        }
        res = requests.post(url, data=body, headers=self.cookies1, verify=False)
        # print(res.headers)
        # print(res.text)
        res_status = res.json()['status']
        # try:
        #     res = int(re.findall(r'"status":(.+\d?)', res.text)[0])
        # except:
        #     print('接口异常，返回数据: '+res.text)
        self.assertEqual(res_status, 2000, msg=res.text)

    @unittest.skip('test_get_applist')
    def test_get_applist(self):
        # print(self.cookies1)
        url = read_config.get_user_info('url') + '/emm-api/app/getAppList.json'
        # print(url)
        body = {
                'loginname': read_config.get_user_info('loginname'),
                'uidmobiledevid': read_config.get_user_info('uidmobiledevid'),
                'tokenid': self.token,
                'devicetype': 'android_phone',
        }
        res = requests.post(url, data=body, headers=self.cookies1, verify=False)
        # res = mock_server.mock_post(requests.post, json.dumps(body), url, body, self.cookies1)
        res_status = res.json()['status']
        # print(res.headers)
        # print(res)
        # try:
        #     res = int(re.findall(r'"status":(.+\d+?)', res.text)[0])
        # except:
        #     print('接口异常，返回数据: '+res.text)
        self.assertEqual(res_status, 2000, msg=res.text)

if __name__ == '__main__':
        unittest.main()