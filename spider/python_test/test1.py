import requests
import json
import re
# r = requests.get('http://www.rainy1012.com/')
#
# # print(r.status_code)
# # #print(r.text)
# # print(r.content)
# # print(r.cookies)
# # print(r.headers)
# # print(r.raw)
#
# #help(requests)
# payload = {
#     'username': 'rainy',
#     'pwd': '123'
# }
# payload_json = json.dumps(payload)
#
# r = requests.post('http://www.rainy1012.com/admin/', json=payload_json)


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:60.0) Gecko/20100101 Firefox/60.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate',
    #'Content-Type': 'application/x-www-form-urlencoded',
    #'Content-Length': '103',
    'Cookie': 'lang=zh-cn; theme=default; lastProduct=1; bugModule=0; preBranch=0; preProductID=1; qaBugOrder=id_desc; keepLogin=on; za=zhujie; zp=bfc4fe55e0b13f85d4ce350fe580e1cc0b5b5db4; windowWidth=1366; windowHeight=631; zentaosid=8vopsimpss4nec5p2pen42ceg4',
    'Connection': 'keep-alive'
}

body = {
    'account': 'zhujie',
    'password': 'e3a98b2bd184d89e5f6c925a37308eaf',
    'keepLogin%5B%5D': 'on',
    'referer': '%2Fzentao%2Fmy.html',
}
s = requests.session()
#r = s.post('http://emmsvn.jianq.com:8080/zentao/user-login-L3plbnRhby9teS5odG1s.html', headers=headers, data=body)
r2 = s.get('http://emmsvn.jianq.com:8080/zentao/my.html', headers=headers)
print(r2.status_code)
print(r2.text)
user = re.findall(r'user"></i> (.+?)&nbsp;', r2.text)
print(user)