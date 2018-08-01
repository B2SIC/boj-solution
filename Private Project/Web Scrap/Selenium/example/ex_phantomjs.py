from selenium import webdriver

# Phantomjs는 기본적으로 CLI 환경이다.
driver = webdriver.PhantomJS("../webdriver/phantomjs/phantomjs")

# 암묵적으로 5초를 기다림. (무조건 5초가 아님, 리소스가 전부 로딩이 되면 빠르면 그냥 넘어감)
# 요청에 대한 데이터가 오지않으면 다음 처리에 예외가 발생하므로 넉넉하게 5초를 기다림.
driver.implicitly_wait(5)

driver.get("http://www.naver.com")
driver.save_screenshot("/home/user/사진/website1.png")

driver.implicitly_wait(5)

driver.get("https://www.daum.net")
driver.save_screenshot("/home/user/사진/website2.png")

driver.quit()

print("스크린샷 완료")


