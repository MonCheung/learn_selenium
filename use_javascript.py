from selenium import webdriver
from time import sleep

#访问百度
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://www.baidu.com')

#搜索
driver.find_element_by_id('kw').send_keys('meizu')
driver.find_element_by_id('su').click()
sleep(2)

#调整窗口大小
driver.set_window_size(500,500)

#调用javascript代码
js='window.scrollTo(100,450)'
driver.execute_script(js)
sleep(3)

driver.quit()
