from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://www.baidu.com')

#鼠标悬停到设置
setting = driver.find_element_by_link_text('设置')
ActionChains(driver).move_to_element(setting).perform()

#打开搜索设置
driver.find_element_by_link_text('搜索设置').click()
sleep(3)

#保存设置
driver.find_element_by_class_name("prefpanelgo").click()
sleep(3)

#接受警告框
driver.switch_to_alert().accept()
sleep(3)

driver.quit()
