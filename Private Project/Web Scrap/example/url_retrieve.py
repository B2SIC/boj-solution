# retrieve : 저장 -> open('r') -> 변수에 할당 -> 파싱 -> 저장
# 파싱이 필요없는 데이터를 바로 저장할 때(다이렉트로 저장)는 urlopen 보다 편리함.

import urllib.request as ur

# URL
imgUrl = "http://blogfiles11.naver.net/20111218_133/oneho5021_1324197876420HxGYB_JPEG/oneho5020_1238175914_49c0fe4de62c2.jpg"
htmlUrl = "http://google.com"

# 저장경로
savePath = "./test.jpg"
savePath2 = "./index.html"

ur.urlretrieve(imgUrl, savePath)
ur.urlretrieve(htmlUrl, savePath2)

print("다운로드 완료 !")
