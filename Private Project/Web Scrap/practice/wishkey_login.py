import requests
from getpass import getpass
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

getId = input("ID: ")
getPw = getpass("PW: ")

# 요청 URL
URL = 'https://www.wishket.com/accounts/login/'

# Fake User-Agent 생성
ua = UserAgent()
# print(ua.ie)
# print(ua.chrome)
# print(ua.random)

with requests.Session() as s:
    # URL 연결
    s.get(URL)

    # Login 정보 Payload
    LOGIN_INFO = {
        'csrfmiddlewaretoken': s.cookies['csrftoken'],
        'identification': getId,
        'password': getPw
    }

    # 요청
    response = s.post(URL, data=LOGIN_INFO, headers={'User-Agent': str(ua.chrome), 'Referer': "https://www.wishket.com/accounts/login/"})

    # HTML 결과 확인
    # print(response.text)

    if response.status_code == 200 and response.ok:
        soup =BeautifulSoup(response.text, 'html.parser')
        projectList = soup.select("table.table.table-responsive > tbody > tr")

        for idx, e in enumerate(projectList, 1):
            print(e.find("th").text, e.find("td").text)
