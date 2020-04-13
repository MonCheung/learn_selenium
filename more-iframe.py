from selenium import webdriver
from time import sleep


driver=webdriver.Chrome()
driver.get('http://www.126.com')

driver.find_element_by_id('lbNormal').click()

#由于iframe每次打开会附带自动变化的id，故直接定位第一个iframe
driver.switch_to_frame(0)
sleep(2)

driver.find_element_by_name('email').clear()
driver.find_element_by_name('email').send_keys('username')
driver.find_element_by_name('password').clear()
driver.find_element_by_name('password').send_keys('password')
driver.find_element_by_id('dologin').click()

#跳回最外层页面
driver.switch_to.default_content()
driver.refresh()

sleep(2)
driver.quit()
