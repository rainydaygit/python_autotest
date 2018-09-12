# /usr/bin/env python
# -*- coding:utf-8 -*-
'''
L = ['A','B','C']
for name in L:
    print('hello '+ name)

while True:
    print (123)
    #continue
    break
    print (456)

li = [11,22,33]
for k,v in enumerate(li, 1):
    print(k,v)
   '''
# 一、元素分类
#
# 有如下值集合 [11,22,33,44,55,66,77,88,99,90...]，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中。
# 即： {'k1': 大于66的所有值, 'k2': 小于66的所有值}
# li = [11,22,33,44,55,66,77,88,99,90]
# dic = {
#     'k1' : [],
#     'k2' : []
# }
# for item in li:
#     if item >= 66:
#         dic['k1'].append(item)
#     else :
#         dic['k2'].append(item)
# print(dic)

# 二、查找
# 查找列表中元素，移除每个元素的空格，并查找以 a或A开头 并且以 c 结尾的所有元素。
# li = ["alec", " aric", "Alex", "Tony", "rain"]
# tu = ("alec", " aric", "Alex", "Tony", "rain")
# dic = {'k1': "alex", 'k2': ' aric',  "k3": "Alex", "k4": "Tony"}
#
# for i in dic.values():
#     i1 = i.strip()
#     #print(i1)
#     if i1.startswith('a') or i1.startswith('A') and i1.endswith('c'):
#         print(i1)

# 三、输出商品列表，用户输入序号，显示用户选中的商品
#     商品 li = ["手机", "电脑", '鼠标垫', '游艇']
# li = ["手机", "电脑", '鼠标垫', '游艇']
# for key,i in enumerate(li):
#     pass
# j = input('请输入序列号：')
# jint = int(j)
# print(li[jint-1])

#五、用户交互，显示省市县三级联动的选择

# dic = {
#     "河北": {
#         "石家庄": ["鹿泉", "藁城", "元氏"],
#         "邯郸": ["永年", "涉县", "磁县"],
#     }
#     "河南": {
#         ...
#     }
#     "山西": {
#         ...
#     }
#
# }
# 四、购物车
# 功能要求：
#
# 要求用户输入总资产，例如：2000
# 显示商品列表，让用户根据序号选择商品，加入购物车
# 购买，如果商品总额大于总资产，提示账户余额不足，否则，购买成功。
# 附加：可充值、某商品移除购物车
'''
goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]
all = int(input('请输入总资产：'))
a = 1
for i in goods:
    print(a,i['name'],i['price'])
    a+=1
dic = {
    'name' : [],
    'price' : []
}
#加入购物车
while True:
    goods_car = int(input('请输入序列号加入购物车：'))
    if goods_car <= len(goods):
        dic['name'].append(goods[goods_car-1]['name'])
        dic['price'].append(goods[goods_car - 1]['price'])
        print(dic)
    else:
        print('商品不存在，请重新选择！')
        continue
    tips = input('继续选择商品&删除商品&去结算？1/2/3：')
    if tips == '1':
        continue
    elif tips == '2':
        del_goods = input('请输入要删除的商品名称：')
        if del_goods in dic['name']:
            #print(dic['name'].index(del_goods))
            dic['price'].pop(dic['name'].index(del_goods))
            dic['name'].remove(del_goods)
            print(dic)
        else:
            print('购物车没有该商品！')
            break
    else:
        break

#print(dic)
#结算
tips2 = input('结算购物车？Y/N：')
while True:
    if tips2 == 'Y' or 'y':
        car_all = 0
        for j in dic['price']:
            car_all = j + car_all
        if all >= car_all:
            all = all - car_all
            print('支付成功，支付金额%d，余额%d'% (car_all,all))
            break
        else:
            print('余额不足，请充值！')
            all1 = int(input('请输入充值金额：'))
            all = all + all1
            print('充值成功，余额%d，正在支付...'% all)
            continue
    else:
        break

#################面向对象编程########################
class Foo:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def kanchai(self):
        print('%s,%s,%s,上山去砍柴'%(self.name,self.age,self.gender))

    def kaiche(self):
        print('%s,%s,%s,开车去东北' % (self.name, self.age, self.gender))

    def baojian(self):
        print('%s,%s,%s,最爱大保健' % (self.name, self.age, self.gender))

a=Foo('小明','10','男')
a.kanchai()
a.kaiche()
a.baojian()


class youxirensheng:
    def __init__(self,name,gender,age,zhandouli):
        self.name = name
        self.gender = gender
        self.age = age
        self.zhandouli = zhandouli

    def chuangjian(self):
        print('%s,%s,%s,初始战斗力%s'%(self.name,self.gender,self.age,self.zhandouli))

    def zhandou(self):
        print('%s,%s,%s,草丛战斗消耗200战斗力'%(self.name,self.gender,self.age))
        self.zhandouli -= 200

    def xiulian(self):
        print('%s,%s,%s,自身修炼增长100战斗力' % (self.name, self.gender, self.age))
        self.zhandouli +=100

    def duoren(self):
        print('%s,%s,%s,多人游戏消耗500战斗力' % (self.name, self.gender, self.age))
        self.zhandouli -=500

cang = youxirensheng('苍井井', '女', 18, 1000)
dong = youxirensheng('东尼木木', '男', 20, 1800)
bo = youxirensheng('波多多', '女', 19, 2500)

cang.zhandou()
dong.xiulian()
bo.duoren()

cang.chuangjian()
dong.chuangjian()
bo.chuangjian()


##############百分比#####################
import sys
import time

def view_bar(num, total):
    rate = float(num) / float(total)
    rate_num = int(rate * 100)
    r = '\r%d%%' % (rate_num, )
    sys.stdout.write(r)
    sys.stdout.flush()

if __name__ == '__main__':
    for i in range(1, 100):
        time.sleep(0.5)
        view_bar(i, 100)

import random
checkcode = ''
for i in range(5):
    current = random.randrange(0,5)
    if current != i:
        temp = chr(random.randint(65,90))
    else:
        temp = random.randint(0,9)
    checkcode += str(temp)
print (checkcode)

class Foo:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def view(self):
        print(self.name)
        print(self.age)
a = Foo('alex',18)
a.view()
'''

# def func_1(n):
#     return func_2(n,1)
#
# def func_2(num, m):
#     if num==1:
#         return m
#     return func_2(num-1, num*m)
#
# a=func_1(4)
# print(a)
#
# def Fi(depth, a1, a2):
#     print(depth, a1)
#     if depth ==20:
#         return 'over'
#     a3 = a1 + a2
#     i = Fi(depth+1, a2, a3)
#     return i
# Fi(1, 0, 1)

# import re
#
# #match:从起始位置开始匹配，匹配成功返回一个对象，未匹配成功返回None
# #text = r'ainy day ! 123'
# text2 = {
#     'a': 'lalala'
# }
# #r = re.match("r\w+", text)
# r = re.match("{'.+'", str(text2))
# rb = re.findall('\'.+\'', str(text2))
# print(rb)
# # print(r.group())  # 获取匹配到的所有结果
# # r = re.match("r(\w+)", text)
# # print(r.groups())  # 获取模型中匹配到的分组结果,元组
# # r = re.match("(?P<n1>r\w+)", text)
# # print(r.groupdict())  # 获取模型中匹配到的分组结果，字典

# import xlrd
# excel_path=r'C:\\test.xlsx'
# data = xlrd.open_workbook(excel_path)
# for i in data._sheet_names:
#     print(i)
#     table = data.sheet_by_name(i)
#     nrows = table.nrows
#     ncols = table.ncols
#     for j in range(0, nrows):
#         for k in range(0, ncols):
#             cell_value = table.cell_value(j, k)
#             # print(cell_value)
#             if cell_value == 22.0:
#                 print(i, j+1, k+1)

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import find_element

driver = webdriver.Chrome()
driver.get('http://192.168.2.32:7070/emm-manager/')
driver.maximize_window()

fi = find_element.findElement(driver)
fi.find_element('username')

fi.find_element('username').clear()
fi.find_element('username').send_keys('secadmin')
fi.find_element('password').clear()
fi.find_element('password').send_keys('emm@2018')
fi.find_element('submit').click()

time.sleep(1)
driver.switch_to.frame('mainframe')
time.sleep(1)
fi.find_element('desktop').click()
time.sleep(1)
# checks = driver.find_elements_by_class_name('portal_checkbox')
checks = fi.find_element('checkbox')
for i in checks:
    i.click()
    time.sleep(1)
fi.find_element('desktop').click()
driver.save_screenshot('首页.png')


time.sleep(3)
driver.close()










