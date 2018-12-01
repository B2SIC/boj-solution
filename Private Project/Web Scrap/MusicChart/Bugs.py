from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://music.bugs.co.kr/chart"
page = urlopen(url).read()
soup = BeautifulSoup(page, 'html.parser')

title = soup.select("table.list.trackList.byChart > tbody > tr th p.title")
artist = soup.select("table.list.trackList.byChart > tbody > \
                     tr td.left p.artist")

for idx, e in enumerate(title, 1):
    print(idx, "위: ", e.find("a")['title'], end=" ")
    print("- ", artist[idx - 1].find("a")['title'])
    