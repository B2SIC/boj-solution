from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://finance.daum.net/"
page = urlopen(url).read()
soup = BeautifulSoup(page, "html.parser")

# print(soup.prettify())

top = soup.select("ul#topMyListNo1 > li")

for idx, e in enumerate(top, 1):
    print(idx, ' >>> ', e.find("a").string, " : ", e.find("span").string)
