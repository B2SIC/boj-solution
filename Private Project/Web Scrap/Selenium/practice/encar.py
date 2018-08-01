from selenium import webdriver

driver = webdriver.Chrome("../webdriver/chrome/chromedriver")
driver.set_window_size(1920, 1280)

driver.get("http://www.encar.com/index.do")

driver.find_element_by_id("manufact").click()
driver.implicitly_wait(3)
driver.find_element_by_xpath('//*[@id="manufactListText"]/ul[2]/li[1]/a').click()
driver.implicitly_wait(3)
driver.find_element_by_xpath('//*[@id="seriesItemList"]/li[2]/a').click()
driver.implicitly_wait(3)
driver.find_element_by_xpath('//*[@id="mdlItemList"]/li[1]/a').click()
driver.implicitly_wait(3)
driver.find_element_by_xpath('//*[@id="indexSch1"]/div[1]/a').click()
