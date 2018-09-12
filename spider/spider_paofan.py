# /usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import re
import json
import time
import xlwt
i=0
for i in range(10):

    j = 28380 +i
    url = 'http://www.chapaofan.com/%s.html' % j
    response = requests.get(url)
    html = response.text
    content = re.findall(r'<h2>(.*?)<span>', html)[0]
    content2 = re.findall(r'<a href="ed2k(.*?)">',html)[0]
    content2 = 'ed2k%s' % content2
    print('电影名称: %s'% content)
    print('下载链接: %s'% content2)
    i+=1

