from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.daum.net"
page = urlopen(url).read()
soup = BeautifulSoup(page, "html.parser")

# 방법 1
keyword = soup.select("ol.list_hotissue.issue_row")[0]

i = 1

for e in keyword:
    if e.find("a") is not -1:
        print(i, e.find("a").string, e.find("a")['href'])
        i += 1

print()

# 방법 2 (tabindex 활용)
top = soup.find_all("a", tabindex="-1")

for idx, k in enumerate(top, 1):
    print(idx, k.string, k.attrs['href'])
