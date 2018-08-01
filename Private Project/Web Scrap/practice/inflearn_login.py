import os
import requests
import getpass
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from urllib.parse import quote_plus

getId = input("ID: ")
getPw = getpass.getpass("PW: ")

# 로그인 유저 정보
LOGIN_INFO = {
    'log': getId,
    'pwd': getPw,
    'user-submit': quote_plus("로그인"),
    'user-cookie': 1
}

# Session 생성, with 구문안에서 유지
with requests.Session() as s:
    login_req = s.post("https://www.inflearn.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.inflearn.com%2F", data=LOGIN_INFO)

    # HTML 소스 확인
    # print(login_req.text)

    # Header 확인
    # print(login_req.headers)

    if login_req.status_code == 200 and login_req.ok:
        post_one = s.get("https://www.inflearn.com/members/" + getId)
        post_one.raise_for_status()
        soup = BeautifulSoup(post_one.text, 'html.parser')
        # print(soup.prettify())
        badges = soup.select("div.badges > ul > li > a > img")
        # print(badges)

        for i, z in enumerate(badges, 1):
            fullFileName = os.path.join("./", str(i) + '.jpg')
            urlretrieve(z['src'], fullFileName)
