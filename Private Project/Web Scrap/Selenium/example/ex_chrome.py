from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")  # CLI 환경으로 바꾸기 (브라우저 생성 없이)

# driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r"../webdriver/chrome/chromedriver")  # CLI 환경으로 실행 하기 위해서 변경
driver = webdriver.Chrome("../webdriver/chrome/chromedriver")  # 눈으로 볼 수 있음

# 윈도우 사이즈 변경 가능
driver.set_window_size(1920, 1280)

driver.get("http://www.google.com")
driver.save_screenshot("/home/user/사진/website_ch1.png")

driver.get("https://www.daum.net")
driver.save_screenshot("/home/user/사진/website_ch2.png")

driver.quit()

print("스크린샷 완료")
