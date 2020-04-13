from selenium import webdriver
import os
import time

#该脚本运行于atom自带的编译插件会报错，无法获取真实的html文件路径

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
