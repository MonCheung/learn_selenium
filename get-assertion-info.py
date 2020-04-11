from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.get('https://www.baidu.com')

print('Befor seach==================')

#打印当前页面title
title=driver.title
print(title)

#打印当前页面url
now_url=driver.current_url
print(now_url)

driver.find_element_by_id('kw').send_keys('16sp')
driver.find_element_by_id('su').click()
sleep(2)

print('After search=================')

#再次打印当前页面title
title=driver.title
print(title)

#打印当前页面url
now_url=driver.current_url
print(now_url)

#获取结果数目
num=driver.find_element_by_class_name('nums_text').text
print(num)


driver.quit()
