# coding=utf-8
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()
driver.get('http://192.168.2.32:7070/emm-manager/')
driver.maximize_window()

driver.find_element_by_id('stroperatorname').clear()
driver.find_element_by_id('stroperatorname').send_keys('secadmin')
driver.find_element_by_id('strpwd').clear()
driver.find_element_by_id('strpwd').send_keys('emm@2018')
driver.find_element_by_id('submitButtom').click()

time.sleep(1)
driver.find_elements_by_class_name('tab-center')[1].click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="menus-container"]/div[2]/div[2]/div[1]').click()
time.sleep(1)
driver.switch_to.frame('mainframe')
time.sleep(1)
driver.find_element_by_class_name('forminput').clear()
driver.find_element_by_class_name('forminput').send_keys('zj')
time.sleep(1)
search_js = "document.getElementsByClassName('l-btn-text search_icon')[0].click();"
# driver.find_element_by_class_name('l-btn-text search_icon').click()
driver.execute_script(search_js)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="datagrid-row-r1-2-0"]/td[1]/div/input').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="devicelist_tbar"]/div[3]/a[1]/span/span').click()
driver.find_elements_by_class_name('menu-text')[0].click()
time.sleep(1)
driver.switch_to.default_content()
driver.find_elements_by_class_name('l-btn-text')[2].click()
time.sleep(1)
driver.find_elements_by_class_name('l-btn-text')[0].click()



time.sleep(3)
driver.close()