from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://www.baidu.com')

#鼠标悬停设置
setting = driver.find_element_by_link_text('设置')
ActionChains(driver).move_to_element(setting).perform()
sleep(2)

#打开搜索设置
driver.find_element_by_link_text('搜索设置').click()
sleep(2)

#操作搜索结果显示条数
num=driver.find_element_by_name('NR')
Select(num).select_by_value('20')
sleep(2)

driver.quit()
