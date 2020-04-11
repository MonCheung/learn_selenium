from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
driver.get('https://www.meizu.com')

#输入框输入内容
driver.find_element_by_tag_name('input').send_keys('166')
time.sleep(3)

#删除多输入的字符
driver.find_element_by_tag_name('input').send_keys(Keys.BACK_SPACE)
time.sleep(3)

#输入覆盖
driver.find_element_by_tag_name('input').send_keys(Keys.SPACE)
driver.find_element_by_tag_name('input').send_keys('sp')
time.sleep(3)

#ctrl+a
driver.find_element_by_tag_name('input').send_keys(Keys.CONTROL,'a')
time.sleep(3)

#ctrl+x
driver.find_element_by_tag_name('input').send_keys(Keys.CONTROL,'x')
time.sleep(3)

#ctrl+v
driver.find_element_by_tag_name('input').send_keys(Keys.CONTROL,'v')
time.sleep(3)

#回车键搜索
driver.find_element_by_tag_name('input').send_keys(Keys.ENTER)
time.sleep(3)

driver.quit()
