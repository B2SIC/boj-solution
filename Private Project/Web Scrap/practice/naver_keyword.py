# parse target = "http://www.naver.com"
# used BeautifulSoup4, urllib

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://www.naver.com'
data = urlopen(url).read()
soup = BeautifulSoup(data, 'html.parser')

keyword_select = soup.select('.ah_a .ah_k')

for i in range(len(keyword_select) // 2):
    print(i + 1, keyword_select[i].getText())
