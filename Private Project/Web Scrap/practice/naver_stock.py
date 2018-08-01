from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/"
page = urlopen(url).read()
soup = BeautifulSoup(page, "html.parser")

top10 = soup.select("#siselist_tab_2 > tr")

i = 1

for e in top10:
    if e.find("a") is not None:
        print(i, e.select_one(".tltle").string)
        i += 1
