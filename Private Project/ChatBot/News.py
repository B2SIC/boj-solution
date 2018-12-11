from urllib.request import urlopen
from urllib import parse
from bs4 import BeautifulSoup


def getNews(keyword):
    url = "https://search.naver.com/search.naver?query=" + parse.quote(keyword) + "&where=news&ie=utf8&sm=nws_hty"
    page = urlopen(url).read()
    soup = BeautifulSoup(page, 'html.parser')

    keyData = soup.select("ul.type01 dt > a")
    dateData = soup.select("ul.type01 dd.txt_inline")

    resultString = ""

    for e in range(len(keyData)):
        findList = dateData[e].text.split()
        for k in range(len(findList)):
            if findList[k] == '전':
                news_date = findList[k - 1] + " " + findList[k]
            elif '.' in findList[k]:
                news_date = findList[k]

        resultString += "기사: " + keyData[e].get('title') + " (" + news_date + ")\n"
        resultString += keyData[e].get('href') + "\n\n"

    return(resultString)


if __name__ == "__main__":
    keyword = input("키워드를 입력해주세요: ")
    print(getNews(keyword))
