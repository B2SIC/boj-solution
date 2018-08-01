from bs4 import BeautifulSoup

html = """
<html>
<body>
<h1>파이썬 BeautifulSoup 공부</h1>
<p>태그 선택자</p>
<p>CSS 선택자</p>
</body>
</html>    
"""

soup = BeautifulSoup(html, 'html.parser')
# print(type(soup))
# print(soup.prettify())

h1 = soup.html.body.h1
print("h1", h1)
print(h1.string)

p1 = soup.html.body.p
print("p1", p1)
print(p1.string)  # 첫번째 노드를 가져옴

p2 = p1.next_sibling.next_sibling # \n 때문에 두 번 해줘야한다.
print("p2", p2)

p3 = p1.previous_sibling.previous_sibling
print("p3", p3)

print("h1 >> ", h1.string)
print("p >> ", p1.string)
print("p >> ", p2.string)
