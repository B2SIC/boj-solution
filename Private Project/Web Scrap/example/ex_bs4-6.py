from bs4 import BeautifulSoup


# using cars.html
def car_func(selector):
    print("car_func", soup.select_one(selector).string)


fp = open("cars.html", encoding="utf-8")
soup = BeautifulSoup(fp, 'html.parser')
car_lambda = lambda x: print("car_lambda", soup.select_one(x).string)

car_func("#gr")
car_func("li#gr")
car_func("ul > li#gr")
car_func("#cars #gr")
car_func("#cars > #gr")
car_func("li[id='gr']")

car_lambda("#gr")
car_lambda("li#gr")
car_lambda("ul > li#gr")
car_lambda("#cars #gr")
car_lambda("#cars > #gr")
car_lambda("li[id='gr']")

print("car_func", soup.select("li")[3].string)
print("car_func", soup.find_all("li")[3].string)
