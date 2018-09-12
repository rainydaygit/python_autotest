#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import re
import json
import urllib3

url = 'https://passport.cnblogs.com/user/signin'

urllib3.disable_warnings()
#发送get请求，访问https需要将verify为假
s =requests.session()
r = s.get(url, verify=False)
# #状态码
# print(r.status_code)
# #文本内容
# print(r.text)
# #转码之后的内容
# print(r.content)
# #响应头
# print(r.headers)
# #响应cookies
# print(r.cookies)

#发送post请求,需要传递请求头，请求体
#请求体有四种类型：json、form-urlencoded、form-data、xml
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0',
    # 'Accept': 'application/json, text/javascript, */*; q=0.01',
    # 'Accept-Language': 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate',
    # 'Content-Type': 'application/json; charset=utf-8',
    # 'X-Requested-With': 'XMLHttpRequest',
    # 'Content-Length': '554',
    # #'Cookie': 'AspxAutoDetectCookieSupport=1; SERVERID=34e1ee01aa40e94e2474dffd938824db|1528987129|1528986437; _ga=GA1.2.979389078.1528986467; _gid=GA1.2.856925118.1528986467; ASP.NET_SessionId=wjgoi2ol0jttmar2drhzugcj',
    # 'Connection': 'keep-alive'
}

# data = {
#     "input1":"KucmmBZ/MBEwsPoBjyz17i2WLrWXRdNDUv/gdBNvOXWvW1wn9xO1F/Uz3HeSq6RJsoaBHC6uHofiQBne++mS/zpEWj6eb1SbVcu2gRosOxuVXEqwyndImM4kNZSzvz5Q/H5ZoOxLhs51LN0lGfxRdcRpSoYw3hRlxjNyGjCgBCQ=",
#     "input2":"OT250Q4mIdXBZatfdpjvX0WKwS+yKj8vV1sAyDkMEY4jWvNSF4c3OmkAi1ID6EeuIg9jj+DEwRzhfgc+d8GyEzlTKR3P/LMlfwXxYOt2EJFT7G4CW+sqv4o1jqpxVVsMbpDvN/SwotCrQY5Rb2IYiHJaEIj5pvjVwui9d2N/EZc=",
#     "remember":'true',
#     "geetest_challenge":"daba9febf22a7ae34eba4cec566eec4b",
#     "geetest_validate":"98753f20117b890404b40f0d1f77f7d6",
#     "geetest_seccode":"98753f20117b890404b40f0d1f77f7d6|jordan"
# }

#添加登录成功后的cookies，模拟登录成功
#使用cookies绕过验证码登陆
c = requests.cookies.RequestsCookieJar()
c.set('.CNBlogsCookie', 'D1BE8A3C8C732DC2EDBD1EC2BC61614009A5BCCC2EF60D4D8D4545FB1CAD4A737D121B90FF31245D230C3C1FB52D01933DD94148FB363E036D760D0D36959D7FBDC8E5E553A1EE2D7EF68FB1D814A8644C8D6937')
c.set('.Cnblogs.AspNetCore.Cookies', 'CfDJ8FHXRRtkJWRFtU30nh_M9mDfmeQIB7uYjN5SLYkjbXFObhLBkoNjRU7OAtfe8uOyITtW3yJwxYcxAxMG5JljbxkPrDsLtxz3tNqhYMjMYrFQs2088XEqMt6HSeryGxB-Vy16bNH39AAm1DB5H0AB8_o7zV_7ttQD_FQh-6RT-3x5JaCOiqzgYPtxDPrFYzEJQkFEhpOYZqYxCP8wUsY2BaJZhO4ODuk-cs6ADoO7zPh_mNLHp2EzN1V0MRe5yVJ9dZnnAIBB27gxMPMuthbAIod_-yXjpypZU8jr_IDmRWW_nV0B1SbM1_peVlQcASs-kA')
c.set('AlwaysCreateItemsAsActive', "True")
c.set('AdminCookieAlwaysExpandAdvanced', "True")
#更新cookies
s.cookies.update(c)
print(s.cookies)

#数据json化
#data_json = json.dumps(data)
r1 = s.get("https://i.cnblogs.com/EditPosts.aspx?opt=1", headers=headers, verify=False)
# 保存草稿箱
url2= "https://i.cnblogs.com/EditPosts.aspx?opt=1"
body = {"__VIEWSTATE": "",
        "__VIEWSTATEGENERATOR":"FE27D343",
        "Editor$Edit$txbTitle":"这是rainy",
        "Editor$Edit$EditorBody":"<p>这里rainy：http://www.cnblogs.com/rainy@/</p >",
        "Editor$Edit$Advanced$ckbPublished":"on",
        "Editor$Edit$Advanced$chkDisplayHomePage":"on",
        "Editor$Edit$Advanced$chkComments":"on",
        "Editor$Edit$Advanced$chkMainSyndication":"on",
        "Editor$Edit$Advanced$txbEntryName":"",
        "Editor$Edit$Advanced$txbExcerpt":"",
        "Editor$Edit$Advanced$tbEnryPassword":"",
        "Editor$Edit$lkbDraft":"存为草稿",
         }
r2 = s.post(url2, data=body, verify=False)
print (r2.text)

# print('=========================')
# r3 = s.get('https://home.cnblogs.com/user/CurrentUserInfo?_=1528990372581', headers=headers, verify=False)
# print(r3.text)
# #正则表达式匹配用户名是否登陆成功
# user = re.findall(r'<a href="/u/1415123/">(.+?)</a>', r3.text)
# print(user[1])
