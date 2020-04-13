from selenium import webdriver

driver=webdriver.Chrome()
driver.get('http://www.baidu.com')

#获取cookie信息
cookie=driver.get_cookies()

#打印cookie信息
print(cookie)

driver.quit()
