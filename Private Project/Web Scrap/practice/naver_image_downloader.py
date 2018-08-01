import os
import errno
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
from urllib.request import urlopen, urlretrieve, build_opener, install_opener

keyword = input("검색어를 입력하세요: ")
url = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query=" + quote_plus(keyword)

savePath = "./download_image/" + keyword

try:
    if not os.path.isdir(savePath):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 만들기 실패 !")
        raise

# Set Header
opener = build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
install_opener(opener)

page = urlopen(url).read()
soup = BeautifulSoup(page, "html.parser")

img_list = soup.select("div.img_area._item > a.thumb._thumb > img")

for idx, img_url in enumerate(img_list, 1):
    fullFileName = os.path.join(savePath, str(idx) + '.jpg')
    urlretrieve(img_url['data-source'], fullFileName)

print("다운로드 완료")
