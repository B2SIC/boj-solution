# parse target = "http://www.naver.com"
# used BeautifulSoup4, urllib

import urllib.request, bs4

url = 'http://www.naver.com'
data = urllib.request.urlopen(url).read()
soup = bs4.BeautifulSoup(data, 'html.parser')
keyword_select = soup.select('.ah_a .ah_k')
for i in range(len(keyword_select) // 2):
    print(i + 1, keyword_select[i].getText())
