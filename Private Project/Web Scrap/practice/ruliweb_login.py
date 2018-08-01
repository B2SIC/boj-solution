import requests
from getpass import getpass
from bs4 import BeautifulSoup

getId = input("ID: ")
getPw = getpass("Pw: ")

# 로그인 유저 정보
LOGIN_INFO = {
    'user_id': getId,
    'user_pw': getPw
}

# Session 생성, with 구문안에서 유지
with requests.Session() as s:
    login_req = s.post("https://user.ruliweb.com/member/login_proc", data=LOGIN_INFO)

    # HTML 소스 확인
    # print(login_req.text)

    # Header 확인
    # print(login_req.headers)

    if login_req.status_code == 200 and login_req.ok:
        post_one = s.get('http://market.ruliweb.com/read.htm?table=market_pcsoft&page=1&num=129102&find=&ftext=')
        post_one.raise_for_status()

        soup = BeautifulSoup(post_one.text, 'html.parser')

        article = soup.select("tr tr > td.con")[1].find_all('span')  # or 'p'

        for e in article:
            if e.string is not None:
                print(e.string)
