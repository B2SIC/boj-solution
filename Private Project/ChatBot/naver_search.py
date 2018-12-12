import json
import re
import urllib.request
from bs4 import BeautifulSoup

CLIENT_ID = ""
CLIENT_SECRET = ""


def Encyclopedia(keyword):
    sendData = ""
    url = "https://openapi.naver.com/v1/search/encyc.json?query=" + urllib.parse.quote(keyword)

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", CLIENT_ID)
    request.add_header("X-Naver-Client-Secret", CLIENT_SECRET)

    response = urllib.request.urlopen(request)
    jsonData = response.read().decode('utf-8')
    dic = json.loads(jsonData)

    for e in range(len(dic['items'])):
        title = dic['items'][e]['title']
        title = re.sub('<.+?>', '', title, 0).strip()
        link = dic['items'][e]['link']
        des = dic['items'][e]['description']
        des = re.sub('<.+?>', '', des, 0).strip()
        sendData += "제목: " + title + "\n"
        sendData += "링크: " + link + "\n"
        sendData += "요약: " + des + "\n\n"

    return sendData


def Movie(keyword):
    sendData = ""
    url = "https://openapi.naver.com/v1/search/movie.json?query=" + urllib.parse.quote(keyword)

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", CLIENT_ID)
    request.add_header("X-Naver-Client-Secret", CLIENT_SECRET)

    response = urllib.request.urlopen(request)
    jsonData = response.read().decode('utf-8')
    dic = json.loads(jsonData)

    for e in range(len(dic['items'])):
        title = dic['items'][e]['title']
        title = re.sub('<.+?>', '', title, 0).strip()
        link = dic['items'][e]['link']
        pubDate = dic['items'][e]['pubDate']
        director = dic['items'][e]['director']
        actor = dic['items'][e]['actor']
        userRating = dic['items'][e]['userRating']

        sendData += "제목: " + title + "\n"
        sendData += "링크: " + link + "\n"
        sendData += "제작년도: " + pubDate + "\n"
        sendData += "감독: " + director + "\n"
        sendData += "출연 배우: " + actor + "\n"
        sendData += "평점: " + userRating + "\n\n"

    return sendData


def Image(keyword):
    sendData = ""
    url = "https://openapi.naver.com/v1/search/image?query=" + urllib.parse.quote(keyword)

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", CLIENT_ID)
    request.add_header("X-Naver-Client-Secret", CLIENT_SECRET)

    response = urllib.request.urlopen(request)
    jsonData = response.read().decode('utf-8')
    dic = json.loads(jsonData)

    for e in range(len(dic['items'])):
        title = dic['items'][e]['title']
        title = re.sub('<.+?>', '', title, 0).strip()
        link = dic['items'][e]['link']
        sendData += "제목: " + title + "\n"
        sendData += "링크: " + link + "\n\n"

    return sendData


def Kin(keyword):
    sendData = ""
    url = "https://openapi.naver.com/v1/search/kin.json?query=" + urllib.parse.quote(keyword)

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", CLIENT_ID)
    request.add_header("X-Naver-Client-Secret", CLIENT_SECRET)

    response = urllib.request.urlopen(request)
    jsonData = response.read().decode('utf-8')
    dic = json.loads(jsonData)

    for e in range(len(dic['items'])):
        title = dic['items'][e]['title']
        title = re.sub('<.+?>', '', title, 0).strip()
        link = dic['items'][e]['link']
        des = dic['items'][e]['description']
        des = re.sub('<.+?>', '', des, 0).strip()
        sendData += "제목: " + title + "\n"
        sendData += "링크: " + link + "\n"
        sendData += "요약: " + des + "\n\n"

    return sendData


if __name__ == "__main__":
    print(Encyclopedia(""))
    print(Movie(""))
    print(Image(""))
    print(Kin(""))
