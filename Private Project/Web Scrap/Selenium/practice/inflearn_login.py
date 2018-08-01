import time
from selenium import webdriver

driver = webdriver.Chrome("../webdriver/chrome/chromedriver")
driver.set_window_size(1920, 1280)
driver.implicitly_wait(3)

driver.get("https://www.inflearn.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.inflearn.com%2F")
time.sleep(5)
driver.implicitly_wait(3)

driver.find_element_by_name('log').send_keys('id')
driver.implicitly_wait(1)
driver.find_element_by_name('pwd').send_keys('pw')
driver.implicitly_wait(1)
driver.find_element_by_xpath('//*[@id="wp-submit"]').click()
