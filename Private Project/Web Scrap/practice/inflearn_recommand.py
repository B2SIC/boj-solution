from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

url = "https://www.inflearn.com/" + quote_plus("추천-강좌")
page = urlopen(url).read()
soup = BeautifulSoup(page, "html.parser")

recommand = soup.select("ul.slides")[0]

for idx, e in enumerate(recommand, 1):
    print(idx, e.select_one("h4.block_title > a").string)
