# coding:utf-8

import os
import configparser

# print(os.path.realpath(__file__))
dir_path = os.path.dirname(os.path.realpath(__file__))
conf_path = os.path.join(dir_path, 'conf.ini')
conf = configparser.ConfigParser()
conf.read(conf_path, encoding='utf-8')

def get_email_info(info):
    res = conf.get('email', info)
    return res

def get_user_info(info):
    res = conf.get('user_info', info)
    return res

def get_postgresl_info(info):
    res = conf.get('postgresql', info)
    return res

def get_element_info(info):
    res = conf.get('element', info)
    return res






