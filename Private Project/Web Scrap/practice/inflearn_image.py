import os
import errno
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
from urllib.request import urlopen, urlretrieve

url = "https://www.inflearn.com/" + quote_plus("추천-강좌")

savePath = "./download_image/"

try:
    if not os.path.isdir(savePath):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 만들기 실패 !")
        raise

page = urlopen(url).read()
soup = BeautifulSoup(page, "html.parser")

img_list = soup.select("ul.slides div.block_media > a > img")
txt_list = soup.select("ul.slides h4.block_title > a")

# 만약 image 링크에 한글이 들어갈 경우 에러 발생함 (본 실습의 범위를 초과하므로 넘어감)
for idx, e in enumerate(img_list):
    fullFileName = os.path.join(savePath, str(idx) + '.jpg')
    # print(e['src'])
    urlretrieve(e.attrs['src'], fullFileName)

for idx, e in enumerate(txt_list):
    with open(savePath + "text_" + str(idx) + ".txt", 'wt') as f:
        f.write(e.string)

print("다운로드 완료")
