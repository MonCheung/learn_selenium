from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://www.baidu.com')

#获得首页窗口句柄
sreach_windows=driver.current_window_handle

driver.find_element_by_link_text('登录').click()
driver.find_element_by_link_text('立即注册').click()

#获得当前所有打开页面句柄
all_handle=driver.window_handles

#进入注册窗口
for handle in all_handle:
    if handle != sreach_windows:
        driver.switch_to_window(handle)
        print('now register windows')
        driver.find_element_by_name('userName').send_keys('username565')
        driver.find_element_by_name('phone').send_keys('13345678952')
        driver.find_element_by_id('TANGRAM__PSP_4__password').send_keys('Tt@123465')
        sleep(3)

driver.quit()
