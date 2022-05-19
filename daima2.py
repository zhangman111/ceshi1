from selenium import webdriver
from time import sleep
import openpyxl
#打开表
excel = openpyxl.load_workbook('../yongli/yongli.xlsx')
#打开表的第一页
sheet = excel['Sheet2']
#print(sheet.values)
i=0

for value in sheet.values:


    driver = webdriver.Chrome()
    # 访问指定的url
    driver.get('http://uml.merlin218.top/')
    driver.find_element_by_xpath('//*[text()="管理员登录"]').click()
    driver.find_element_by_xpath('//input[@type="text"]').send_keys('admin')
    driver.find_element_by_xpath('//input[@type="password"]').send_keys('admin')
    driver.find_element_by_xpath('//button[text()="登录"]').click()
    sleep(1)
    driver.find_element_by_xpath('//*[text()="账号维护"]').click()
    driver.find_element_by_xpath('//*[text()="创建管理员"]').click()

    driver.find_element_by_xpath('//input[@placeholder="请输入用户名"]').send_keys(value[1])

    driver.find_element_by_xpath('//input[@placeholder="请输入密码"]').send_keys(value[2])


    driver.find_element_by_xpath('//input[@placeholder="请重复输入密码"]').send_keys(value[2])
    driver.find_element_by_xpath('//button[text()="提交"]').click()
    print(value[0])
    print("用例通过")






