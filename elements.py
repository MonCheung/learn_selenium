from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.get('http:www.baidu.com')

driver.find_element_by_id('kw').send_keys('meizu')
driver.find_element_by_id('su').click()
sleep(2)

#定为一组元素
texts=driver.find_elements_by_xpath('//div/h3/a')

#循环遍历每一个搜索结果的标题
for t in texts:
    print(t.text)

sleep(5)
driver.quit()
