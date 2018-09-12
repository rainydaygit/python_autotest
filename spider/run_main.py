# coding:utf-8
import unittest
import os
import time
import requests
import re
import urllib3
from common import send_email
from report import HTMLTestRunner_cn
from ruamel import yaml
from config import read_yaml, read_config
from common.logger import Log

urllib3.disable_warnings()
dir_path = os.path.dirname(os.path.realpath(__file__))
ti = int(time.time())
class RunMain:

    def login(self):

        url = read_config.get_user_info('url')+'/emm-api/authorization/login.json'
        body = {
            'loginname': read_config.get_user_info('loginname'),
            'password': read_config.get_user_info('password'),
            'uidmobiledevid': read_config.get_user_info('uidmobiledevid'),
            'devicetype': 'android_phone',
            'strimagecode': '1234',
            'clientsubmittime': ti,
            'isfirstlogin': '0',
            'clientversion': '2.3.2'
        }
        res = requests.post(url, data=body, verify=False)
        # print(res.headers)
        # print(res.text)

        tokenid = re.findall(r'"tokenid":"(.+?)"', str(res.text))[0]
        sessionid = re.findall(r'JSESSIONID=(.+?);', str(res.headers))[0]

        return tokenid, sessionid

        # print(tokenid, sessionid)

    def write_yaml(self, value, cookies1):

        token_path = os.path.join(dir_path, 'config', 'token.yaml')
        token = {'token': value,
                 'cookies': cookies1
                 }
        with open(token_path, 'w', encoding='utf-8') as f:
            yaml.dump(token, f, Dumper=yaml.RoundTripDumper)


    def add_case(self, casename='case', rule='test*.py'):
        # 获取当前路径下，case的目录
        case_path = os.path.join(dir_path, casename)
        # 加载case目录下面的所有test开头的用例
        discover = unittest.defaultTestLoader.discover(case_path, pattern=rule, top_level_dir=None)

        return discover

    def run_case(self, allcase, reportname='report'):
        # 获取当前时间
        now = time.strftime('%Y_%m_%d_%H_%M_%S')
        # 获取report目录
        report_path = os.path.join(dir_path, reportname)
        if not os.path.exists(report_path):os.mkdir(report_path)
        report_abspath = os.path.join(report_path, now+'_test_report.html')
        # 执行测试用例，生成测试报告
        with open(report_abspath, 'wb') as f:
            runner = HTMLTestRunner_cn.HTMLTestRunner(stream=f, title='自动化测试报告，测试结果：', description='用例执行情况：')
            runner.run(allcase)

    def get_new_report(self):
        report_path = os.path.join(dir_path, 'report')
        report_list = os.listdir(report_path)
        # 根据报告的修改时间排序
        report_list.sort(key=lambda fn: os.path.getmtime(os.path.join(report_path, fn)))
        # 获取最后一个report，即最新的报告
        report_file = os.path.join(report_path, report_list[-1])

        return report_file


if __name__ == '__main__':

    # ru = RunMain()
    # ru.login()
    # ru_case = ru.add_case()
    # ru.run_case(ru_case)

    log = Log()
    ru = RunMain()
    try:
        rl, r2 = ru.login()
        ru.write_yaml(rl, r2)
        token1 = read_yaml.get_token()
    except:
        log.error('获取token失败！')
    ru_case = ru.add_case()
    ru.run_case(ru_case)
    newre = ru.get_new_report()
    se = send_email.sendEmail(['zhujie@jianq.com', '15999635992@163.com'])
    #se.send_email_text('这是主题', '这是内容！！！！')
    se.send_email_multipart('带附件的主题!!!!!', newre)

