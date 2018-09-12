import os
#import re

#递归查询目录
def func_1(n):
    return func_2(n,1)

def func_2(num,m):
    if num == 1:
        return m
    return func_2(num-1,m*num)

#读log文件，找error内容写到文件
def readfile():
    file_1=[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.log']
    print(file_1)

#dir_1=os.path.abspath('.')
'''
path_1='C:\\Users\\Administrator\\PycharmProjects\\spider'
dir_2=[x for x in os.listdir(path_1) if os.path.isdir(x)]
for i in dir_2:
    path_1 = 'C:\\Users\\Administrator\\PycharmProjects\\spider'
    dir_3 = [x for x in os.listdir(path_1) if os.path.isdir(x)]
    path_1=os.path.join(path_1,i)
    print(path_1)
    print(dir_3)

#print(dir_1)
print(dir_2)
'''