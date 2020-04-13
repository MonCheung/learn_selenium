from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


driver=webdriver.Chrome()
driver.get('http://www.baidu.com')

element=WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.ID,'kw')))

element.send_keys('selenium')
sleep(3)

driver.quit()
