from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
'''
driver.find_element_by_id("kw").clear()
driver.find_element_by_id("kw").send_keys("meizu")
driver.find_element_by_id("su").click()

time.sleep(10)
'''
#获取输入框尺寸
Size=driver.find_element_by_id('kw').size
print(Size)

#返回页面底部备案信息
text=driver.find_element_by_id('s-bottom-layer-right').text
print(text)

#返回元素属性值
attribute=driver.find_element_by_id('kw').get_attribute('type')
print(attribute)

#查看返回元素是否可见
result=driver.find_element_by_id('s-bottom-layer-right').is_displayed()
print(result)

time.sleep(10)

driver.quit()
