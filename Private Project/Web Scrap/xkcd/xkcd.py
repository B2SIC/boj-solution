'''
CSS Select Method Usage

soup.select('div') : <div> 태그가 붙은 모든 엘리먼트
soup.select('#author') : id 속성이 author 인 엘리먼트
soup.select('.notice') : CSS class 속성이 notice 라는 이름을 가진 모든 엘리먼트
soup.select('div span') : <div> 태그가 붙은 모든 엘리먼트 안에있는 <span> 태그가 붙은 엘리먼트
soup.select('div > span') : <div> 태그가 붙은 모든 엘리먼트 안에 있는, 바로 다음 단계의 <span> 엘리먼트
즉 이 두 엘리먼트 사이에 어떤 다른 엘리먼트도 없어야 한다.
soup.select('input[name]') : <input> 태그가 붙은 모든 엘리먼트로, name 속성을 가지고 있으며 그 값은 무엇이든 관계 없다.
soup.select('input[type="button"]') : <input> 태그가 붙은 모든 엘리먼트로, type 이라는 속성을 가지고 있으며, 그 값은 button 이어야 한다.
'''

import requests, bs4, os

url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)  # exist_ok : 폴더가 이미 존재 할 경우 예외를 던지는 것을 막을 수 있다.

while not url.endswith('#'):
    print("Downloading page %s ..." % url)
    res = requests.get(url)
    res.raise_for_status()  # 문제가 있는 페이지일 경우 에러를 던진다. (아닐경우, 즉 OK 면 아무일도 하지 않음)

    soup = bs4.BeautifulSoup(res.text, 'lxml')

    comicElem = soup.select('#comic img')
    if comicElem == []:
        print("Could not find comic image.")
    else:
        comicUrl = "http:" + comicElem[0].get('src')
        print("Downloading image %s ..." % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()

        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')

        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

        prevLink = soup.select('a[rel="prev"]')[0]
        url = 'http://xkcd.com' + prevLink.get('href')

print("Done.")
