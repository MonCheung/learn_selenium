from selenium import webdriver
import os
import time


driver=webdriver.Chrome()
file_path='file:///' + os.path.abspath('.') +'\\upfile.html'
print('打开文件路径：' + file_path)

upfile_path=os.path.abspath('.')+'\\upfile.txt'
print('上传文件路径：' + upfile_path)

driver.get(file_path)
time.sleep(5)

#定位上传按钮，添加本地文件
driver.find_element_by_name('file').send_keys(upfile_path)
time.sleep(5)

driver.quit()
