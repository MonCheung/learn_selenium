from selenium import webdriver
driver = webdriver.Chrome()
#driver.maximize_window()

frist_url="https://www.baidu.com/"
print('now access %s' %(frist_url))
driver.get(frist_url)

second_url="https://news.baidu.com/"
print('now access %s' %(second_url))
driver.get(second_url)

print('back to %s' %(frist_url))
driver.back()

print('forward to %s' %(second_url))
driver.forward()

driver.quit()
