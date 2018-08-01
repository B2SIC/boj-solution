from bs4 import BeautifulSoup

html = """
<html><body>
    <ul>
        <li><a href="http://www.naver.com">naver</a></li>
        <li><a href="http://www.daum.net">daum</a></li>
        <li><a href="http://www.daum.com">daum</a></li>
        <li><a href="http://www.google.com">google</a></li>
        <li><a href="http://www.tistory.com">tistory</a></li>
    </ul>
</body></html>        
"""

soup = BeautifulSoup(html, 'html.parser')

links = soup.find_all("a")

a = soup.find_all("a", string="daum")
print('a', a)

b = soup.find_all("a", limit=3)
print('b', b)

c = soup.find_all(string=["naver", "google"])
print('c', c)

for i in links:
    # print('a', type(i), i)
    href = i.attrs['href']
    txt = i.string
    # print('txt >> ', txt, "href >> ", href)
