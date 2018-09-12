# -*- coding:utf-8 -*-

import requests
import re
import urllib3

urllib3.disable_warnings()
host = 'https://demo3.appiron.cn:30443'
url = host + '/emm-manager/login/login.do'
#print(url)

# r = requests.get(url='https://demo3.appiron.cn:30443/emm-manager/', verify=False)
# #print(r.cookies)
# r_cookies = requests.utils.dict_from_cookiejar(r.cookies)['JSESSIONID']
# #print(r_cookies)
# r_cookies_str = 'JSESSIONID=' + r_cookies
data = {
    'strname': 'secadmin',
    'strpwd': '150,36,10,215,125,37,204,185'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Length': '66',
    # 'Cookie': r_cookies_str,
    'Cookie': 'JSESSIONID=15CEC8C269490A5C1ADCD77F2BFBDF95',
    'Connection': 'keep-alive'
}
# s = requests.session()
#
# c = requests.cookies.RequestsCookieJar()
# c.set('JSESSIONID', r_cookies)
# s.cookies.update(c)
#
# s = s.post(url=url, data=data, headers=headers, verify=False)
s = requests.post(url=url, data=data, headers=headers, verify=False)
print(s.status_code)
print(s.text)