# coding:utf-8
# import yaml
import os
from ruamel import yaml

cur = os.path.dirname(os.path.realpath(__file__))

def get_token(yamlName="token.yaml"):
    '''
    从token.yaml读取token值
    :param yamlName: 配置文件名称
    :return: token值
    '''
    p = os.path.join(cur, yamlName)
    f = open(p, encoding='utf-8')
    a = f.read()
    t = yaml.load(a, Loader=yaml.Loader)
    f.close()
    return t["token"], t['cookies']

if __name__ == "__main__" :
    print(get_token())