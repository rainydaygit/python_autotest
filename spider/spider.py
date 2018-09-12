# /usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import re
import json
import time
import xlwt
#import matplotlib

DATA = []
url = 'https://s.taobao.com/search?q=Python&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306'

#发送请求
response = requests.get(url)

#获取html源码
html = response.text
#print(response.text)

#正则表达式提取商品信息
content = re.findall(r'g_page_config = (.*?)g_srp_loadCss', html, re.S)[0].strip()[:-1]
#print(content)

#格式化json
content = json.loads(content)
#print(content)

data_list = content['mods']['itemlist']['data']['auctions']
for item in data_list:
    temp = {
        'title': item['title'],
        'view_price': item['view_price'],
        'view_sales': item['view_sales'],
        'view_fee': '否' if float(item['view_fee']) else '是',
        'isTmall': '是' if item['shopcard']['isTmall'] else '否',
        'item_loc': item['item_loc'],
        'detail_url': item['detail_url'],
        'nick': item['nick'],

    }
    DATA.append(temp)

#cookies保持
cookies=response.cookies
#异步加载的数据
url2 = 'https://s.taobao.com/api?_ksTS=1522736332616_238&callback=jsonp239&ajax=true&m=customized&sourceId=tb.index&q=Python&spm=a21bo.2017.201856-taobao-item.1&s=36&imgfile=&initiative_id=tbindexz_20170306&bcoffset=0&commend=all&ie=utf8&rn=814f795007ce4dfc59a37cde657df45f&ssid=s5-e&search_type=item'
response2 = requests.get(url2 , cookies=cookies)
html2 = response2.text
content = re.findall(r'{.*}', html2)[0]

content = json.loads(content)
data_list = content['API.CustomizedApi']['itemlist']['auctions']
for item in data_list:
    temp = {
        'title': item['title'],
        'view_price': item['view_price'],
        'view_sales': item['view_sales'],
        'view_fee': '否' if float(item['view_fee']) else '是',
        'isTmall': '是' if item['shopcard']['isTmall'] else '否',
        'item_loc': item['item_loc'],
        'detail_url': item['detail_url'],
        'nick': item['nick'],

    }
    DATA.append(temp)

cookies = response2.cookies
for i in range(1, 10):
    ktsts = time.time()
    _ksTS = '%s_%s' % (int(ktsts*1000), str(ktsts)[-3:])
    callback = 'jsonp%s' % (int(str(ktsts)[-3:])+1)
    data_value = 44 * i
    url = 'https://s.taobao.com/search?data-key=s&data-value={}&ajax=true&_ksTS={}&callback={}&q=Python&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=4&ntoffset=4&p4ppushleft=1,48&s=44'.format(data_value, _ksTS, callback)
    response3 = requests.get(url, cookies = cookies)
    html3 = response3.text

    content = re.findall(r'{.*}', html3)[0]
    #print(content)

    # 格式化json
    content = json.loads(content)
    # print(content)

    data_list = content['mods']['itemlist']['data']['auctions']
    for item in data_list:
        temp = {
            'title': item['title'],
            'view_price': item['view_price'],
            'view_sales': item['view_sales'],
            'view_fee': '否' if float(item['view_fee']) else '是',
            'isTmall': '是' if item['shopcard']['isTmall'] else '否',
            'item_loc': item['item_loc'],
            'detail_url': item['detail_url'],
            'nick': item['nick'],

        }
        DATA.append(temp)

f = xlwt.Workbook(encoding = 'utf-8')
worksheet = f.add_sheet('sheet01', cell_overwrite_ok=True)

worksheet.write(0, 0, '标题')
worksheet.write(0, 1, '价格')
worksheet.write(0, 2, '购买人数')
worksheet.write(0, 3, '是否包邮')
worksheet.write(0, 4, '是否天猫')
worksheet.write(0, 5, '地区')
worksheet.write(0, 6, '店名')
worksheet.write(0, 7, 'url')

for i in range(len(DATA)):
    worksheet.write(i + 1, 0, DATA[i]['title'])
    worksheet.write(i + 1, 1, DATA[i]['view_price'])
    worksheet.write(i + 1, 2, DATA[i]['view_sales'])
    worksheet.write(i + 1, 3, DATA[i]['view_fee'])
    worksheet.write(i + 1, 4, DATA[i]['isTmall'])
    worksheet.write(i + 1, 5, DATA[i]['item_loc'])
    worksheet.write(i + 1, 6, DATA[i]['nick'])
    worksheet.write(i + 1, 7, DATA[i]['detail_url'])

f.save('淘宝搜索Python的结果.xls')











