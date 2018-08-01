# urlopen : 변수 할당 -> 파싱 -> 저장

import urllib.request as ur

# URL
imgUrl = "http://blogfiles11.naver.net/20111218_133/oneho5021_1324197876420HxGYB_JPEG/oneho5020_1238175914_49c0fe4de62c2.jpg"
htmlUrl = "http://google.com"

# 저장경로
savePath = "./test.jpg"
savePath2 = "./index.html"

f = ur.urlopen(imgUrl).read()
f2 = ur.urlopen(htmlUrl).read()

saveFile1 = open(savePath, 'wb')  # w : write, r : read, a : add, b : binary
saveFile1.write(f)
saveFile1.close()

with open(savePath2, 'wb') as saveFile2:
    saveFile2.write(f2)

print("다운로드 완료 !")
