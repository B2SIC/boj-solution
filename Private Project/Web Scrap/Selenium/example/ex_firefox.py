from selenium import webdriver
from selenium.webdriver.firefox.options import Options

firefox_options = Options()
firefox_options.add_argument("--headless")  # CLI 환경으로 바꾸기 (브라우저 생성 없이)

driver = webdriver.Firefox(firefox_options=firefox_options, executable_path=r"../webdriver/firefox/geckodriver")  # CLI 환경으로 실행 하기 위해서 변경

# 윈도우 사이즈 변경 가능
driver.set_window_size(1920, 1280)

driver.get("http://www.google.com")
driver.save_screenshot("/home/user/사진/website_ch1.png")

driver.get("https://www.daum.net")
driver.save_screenshot("/home/user/사진/website_ch2.png")

driver.quit()

print("스크린샷 완료")
