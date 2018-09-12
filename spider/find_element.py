# coding = utf-8
from selenium import webdriver
from config import read_config

class findElement(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, key):
        data = read_config.get_element_info(key)
        by = data.split('>')[0]
        value = data.split('>')[1]
        try:
            if by == 'id':
                return self.driver.find_element_by_id(value)
            elif by == 'name':
                return self.driver.find_element_by_name(value)
            elif by == 'classname':
                return self.driver.find_element_by_class_name(value)
            elif by == 'classnames':
                return self.driver.find_elements_by_class_name(value)
            else:
                return self.driver.find_element_by_xpath(value)
        except:
            return None

