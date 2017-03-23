#coding:utf-8

#计算M2同比增速

import selenium
from selenium import webdriver
import time
import re

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
browser = webdriver.Chrome(chrome_options=options)
url = 'http://www.pbc.gov.cn/diaochatongjisi/116219/index.html'
browser.get(url)
browser.maximize_window()
time.sleep(3)

print ('准备打开2017年数据：')
time.sleep(3)
browser.find_element_by_xpath(".//*[@id='c_con']/table[2]/tbody/tr/td/table/tbody/tr[1]/td/a").click()
time.sleep(3)

handles = browser.window_handles
browser.switch_to_window(handles[1])

print browser.title  #现在进入的窗口是最新的
# browser.find_element_by_xpath(".//*[@id='11863']/tbody/tr/td[1]/input").send_keys('123')
browser.find_element_by_xpath(".//*[@id='f8522e94cf7a4ca7aff09dc41c349af6']/div[2]/table[5]/tbody/tr/td/a").click()
time.sleep(3)
handles = browser.window_handles
browser.switch_to_window(handles[1])
browser.find_element_by_xpath(".//*[@id='con']/table[3]/tbody/tr/td/table[5]/tbody/tr/td[2]/a").click()
time.sleep(3)
handles = browser.window_handles
# print (handles)
browser.switch_to_window(handles[2])
# print browser.page_source
time.sleep(2)
response = browser.page_source
pattern = re.compile(r'x:num=".*">(.*?)</td>')
result = re.findall(pattern,response)
print result
#计算M2数据
M2 = (float(result[13])-float(result[12]))/float(result[12])
print(M2)