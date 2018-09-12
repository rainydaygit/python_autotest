# -*- coding:utf-8 -*-

import requests
import re
import urllib3

urllib3.disable_warnings()
host = 'https://demo3.appiron.cn:30443'
url = host + '/emm-manager/'
#print(url)
r = requests.get(url=url, verify=False)
print(r.status_code)
print(r.text)
print(r.cookies)
