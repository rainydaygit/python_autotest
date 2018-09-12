# coding=utf-8
import unittest
import os
#import yaml
from common import HTMLTestRunner_cn
from ruamel import yaml

curpath = os.path.dirname(os.path.realpath(__file__))

def login(user="yoyo", psw="123456"):
    '''
    先执行登录，传账号和密码两个参数
    :return: 返回token值
    '''
    print("登录的账号名称：%s" % user)
    p = psw
    print("输入的密码：**********")
    token = "xxxxxxxxx"     # 登录后获取到的token值
    return token

def write_yaml(value):
    '''
    把获取到的token值写入到yaml文件
    :param value:
    :return:
    '''
    ypath = os.path.join(curpath, "common", "token.yaml")
    print(ypath)
    # 需写入的内容
    t = {"token": value}
    # 写入到yaml文件
    with open(ypath, "w", encoding="utf-8") as f:
        yaml.dump(t, f, Dumper=yaml.RoundTripDumper)

def all_case(rule="test*.py"):
    '''加载所有的测试用例'''
    case_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "case")
    # 定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(case_path,
                                                  pattern=rule,
                                                  top_level_dir=None)
    return discover


def run_case(all_case, reportName="report"):
    '''
    执行所有的用例, 并把结果写入HTML测试报告
    '''
    curpath = os.path.dirname(os.path.realpath(__file__))
    report_path = os.path.join(curpath, reportName)  # 用例文件夹
    # 如果不存在这个report文件夹，就自动创建一个
    if not os.path.exists(report_path):os.mkdir(report_path)
    report_abspath = os.path.join(report_path, "result.html")
    print("report path:%s"%report_abspath)
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner_cn.HTMLTestRunner( stream=fp,
                                               verbosity=2,
                                               title=u'自动化测试报告,测试结果如下：',
                                               description=u'用例执行情况：')

    # 调用add_case函数返回值
    runner.run(all_case)
    fp.close()

if __name__ == "__main__":
    token = login("admin", "111111")  # 1.登录
    write_yaml(token)                   # 2.写入yaml
    allcases = all_case()                  # 3.加载用例
    run_case(allcases)


