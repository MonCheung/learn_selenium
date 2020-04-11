from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver=webdriver.Chrome()
driver.get('https://www.meizu.com')

above=driver.find_element_by_link_text('声学')

ActionChains(driver).move_to_element(above).perform()
time.sleep(3)

ActionChains(driver).context_click(above).perform()
time.sleep(3)

ActionChains(driver).click(above).perform()
time.sleep(5)

driver.quit()
