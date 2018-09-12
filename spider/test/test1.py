# coding:utf-8
import os
import re

'''
    1.walk方法，传入path，返回三个参数：所有的文件夹路径、所有的目录名称、所有的文件名称
    2.使用for循环遍历所有目录，拼接文件夹路径+文件名称
    3.查找.log结尾的文件，打开，使用正在表达式查找error字段
    4.将所有内容写到txt文件里面
'''
path = os.path.dirname(os.path.realpath(__file__))
# print(path)
def find_error(path):
    for fpath, dirname, fname in os.walk(path):
        for f in fname:
            filename = os.path.join(fpath, f)
            if filename.endswith('.log'):
                with open(filename, 'r', encoding='gbk') as fp:
                    a = fp.read()
                    error = re.findall('error:(.+?)\n', a)
                    for j in error:
                        with open('1.txt', 'a') as f:
                            f.write(j)
                            f.write('\n')
                    print(error)
                # print(filename)
            # print(fname)

find_error(path)