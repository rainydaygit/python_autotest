# -*- coding:utf-8 -*-

import requests
import urllib3

urllib3.disable_warnings()

host = 'https://demo3.appiron.cn:30443'
url = host + '/emm-manager/secpolicy/savePolicy.do'

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

data = {
    'formData': '{"mobilecheckapplist0":[],"mobilecheckapplist2":[],"mobilecheckapplist3":[],"mobilecheckapplist4":[],"disableWIFIlist":[],"onlyallowWIFIlist":[]}',
    'isecpolicytype': '903',
    'strsecpolicyname': '安全检查策略测试2',
    'istatus': '1',
    'isecpolicylevel': '50',
    'uidscheduleid': '1',
    'ipwdbefnumsame': '1',
    'app_scopes': '[{"rowindex":"","gridid":"#appliedRangeGrid","uidrecordid":"","idevaddrtype":"0","strdevgip":"","strdevip1":"","uiddevgroupid":"","uiddeptid":"","uiduserid":"","uidusergroupid":"","strdesc":""}]',
    'recordLogData': '%E7%AD%96%E7%95%A5%E5%90%8D%E7%A7%B0%EF%BC%9A%3Cfont%20style%3D%22color%3Ablue%3B%22%3E%3C%2Ffont%3E%20%E4%BF%AE%E6%94%B9%E4%B8%BA%20%E7%AD%96%E7%95%A5%E5%90%8D%E7%A7%B0%EF%BC%9A%3Cfont%20style%3D%22color%3Ablue%3B%22%3E%E5%AE%89%E5%85%A8%E6%A3%80%E6%9F%A5%E7%AD%96%E7%95%A5%E6%B5%8B%E8%AF%951%3C%2Ffont%3E%3Cbr%3E%E7%AD%96%E7%95%A5%E4%B8%8B%E5%8F%91%E8%8C%83%E5%9B%B4%20%E4%BF%AE%E6%94%B9%E6%83%85%E5%86%B5%EF%BC%9A%3Cbr%3E%3Ctable%20style%3D%22border-collapse%3Acollapse%3Bwidth%3A400px%3Bword-break%3Abreak-all%3Bwhite-space%3Apre-line%3B%22%20class%3D%22table%22%3E%3Ctbody%3E%3Ctr%3E%3Cth%20style%3D%22border%3A%201px%20solid%20rgb(173%2C%20216%2C%20230)%3B%22%3E%E6%93%8D%E4%BD%9C%E5%8A%A8%E4%BD%9C%3C%2Fth%3E%3Cth%20style%3D%22border%3A%201px%20solid%20rgb(173%2C%20216%2C%20230)%3B%22%3E%E7%AE%A1%E7%90%86%E5%AF%B9%E8%B1%A1%3C%2Fth%3E%3Cth%20style%3D%22border%3A%201px%20solid%20rgb(173%2C%20216%2C%20230)%3B%22%3E%E5%AF%B9%E8%B1%A1%E7%B1%BB%E5%9E%8B%3C%2Fth%3E%3Cth%20style%3D%22border%3A%201px%20solid%20rgb(173%2C%20216%2C%20230)%3B%22%3E%E5%80%BC%3C%2Fth%3E%3Cth%20style%3D%22border%3A%201px%20solid%20rgb(173%2C%20216%2C%20230)%3B%22%3E%E6%8F%8F%E8%BF%B0%3C%2Fth%3E%3Cth%20style%3D%22border%3A%201px%20solid%20rgb(173%2C%20216%2C%20230)%3B%22%3E%E6%93%8D%E4%BD%9C%3C%2Fth%3E%3C%2Ftr%3E%3Ctr%3E%3Ctd%20style%3D%22border%3A%201px%20solid%20rgb(173%2C%20216%2C%20230)%3B%22%3E%E6%96%B0%E5%A2%9E%3C%2Ftd%3E%3Ctd%20style%3D%22border%3A%201px%20solid%20rgb(173%2C%20216%2C%20230)%3B%22%3E%E8%AE%BE%E5%A4%87%3C%2Ftd%3E%3Ctd%20style%3D%22border%3A%201px%20solid%20rgb(173%2C%20216%2C%20230)%3B%22%3E%E6%89%80%E6%9C%89%E8%AE%BE%E5%A4%87%3C%2Ftd%3E%3Ctd%20style%3D%22border%3A%201px%20solid%20rgb(173%2C%20216%2C%20230)%3B%22%3E%3C%2Ftd%3E%3Ctd%20style%3D%22border%3A%201px%20solid%20rgb(173%2C%20216%2C%20230)%3B%22%3E%3C%2Ftd%3E%3Ctd%20style%3D%22border%3A%201px%20solid%20rgb(173%2C%20216%2C%20230)%3B%22%3E%3Ca%3E%E7%BC%96%E8%BE%91%3C%2Fa%3E%3C%2Ftd%3E%3C%2Ftr%3E%3C%2Ftbody%3E%3C%2Ftable%3E',
    'isajax': '1'
}

r = requests.post(url=url, headers=headers, data=data, verify=False)
print(r.status_code)
print(r.text)
