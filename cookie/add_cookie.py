from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://www.baidu.com')

#向cookie写入内容
driver.add_cookie({'name':'testaaa','value':'testbbb'})

#遍历cookie信息并打印
for cookie in driver.get_cookies():
    print('%s -> %s' %(cookie['name'],cookie['value']))

sleep(5)
driver.quit()
