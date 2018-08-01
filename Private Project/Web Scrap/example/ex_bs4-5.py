from bs4 import BeautifulSoup

# using food-list.html

fp = open("food-list.html", encoding="utf-8")
soup = BeautifulSoup(fp, 'html.parser')

print("1", soup.select_one("li:nth-of-type(8)").string)
print("2", soup.select_one("#ac-list > li:nth-of-type(4)").string)
print("3", soup.select("#ac-list > li[data-lo='cn']")[0].string)
print("4", soup.select("#ac-list > li.alcohol.high")[0].string)

param = {"data-lo": "cn", "class": "alcohol"}
# 쉽게 접근
print("5", soup.find("li", param).string)
# 정확하게 접근
print("6", soup.find(id="ac-list").find("li", param).string)

for ac in soup.find_all("li"):
    if ac['data-lo'] == 'us':
        print('data-lo == us', ac.string)
