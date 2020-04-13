from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.get('http://www.baidu.com')

driver.find_element_by_id('kw').send_keys('meizu')
driver.find_element_by_id('su').click()
sleep(2)

#截取当前窗口图片
driver.get_screenshot_as_file('D:\\baidu_img.png')

driver.quit()
