import time
import getpass
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class NCafeWriteAtt:
    # 초기화 실행(webdrvier 설정)
    def __init__(self, id, pw):
        chrome_options = Options()
        # CLI (User-Agent 에 Chrome headlessChrome 로 날라감, 만약 이걸 차단 한다면 fake-useragent를 사용해야함)
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(chrome_options=chrome_options,
                                       executable_path="../webdriver/chrome/chromedriver")
        self.driver.implicitly_wait(5)

        self.id = id
        self.pw = pw

    # 네이버 카페 로그인 && 출석 체크
    def writeAttendCheck(self):
        self.driver.get("https://nid.naver.com/nidlogin.login")
        self.driver.find_element_by_name('id').send_keys(self.id)
        self.driver.find_element_by_name('pw').send_keys(self.pw)
        self.driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
        self.driver.implicitly_wait(30)
        self.driver.get("https://cafe.naver.com/goondae/AttendanceView.nhn?search.clubid=10797658&search.menuid=10")
        self.driver.implicitly_wait(30)
        self.driver.switch_to.frame('cafe_main')
        self.driver.find_element_by_id('cmtinput').send_keys('출석체크 !')
        self.driver.find_element_by_xpath('//*[@id="main-area"]/div[6]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/a/img').click()

        time.sleep(3)

    # 소멸자
    def __del__(self):
        # self.driver.close() # 현재 실행 포커스(로그인 => 카페 이동 => 프레임 Switch) 된 영역을 종료
        self.driver.quit() # Selenium 전체 프로그램 종료
        print("Removed driver Object")

# 실행
if __name__ == "__main__":
    # 아이디 비밀번호 입력
    getId = input("ID: ")
    getPw = getpass.getpass("PW: ")

    # 객체 생성
    work =  NCafeWriteAtt(getId, getPw)

    # 시작 (시간 측정)
    start = time.time()

    # 프로그램 실행
    work.writeAttendCheck()

    # 종료
    print("-- Total %s seconds --" % (time.time() - start))

    # 객체 소멸
    del work  # 꼭 안해도 되긴 함.
