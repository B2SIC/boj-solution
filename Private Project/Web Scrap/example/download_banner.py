import urllib.request as req

imgUrl = "https://ssl.pstatic.net/tveta/libs/1202/1202699/0c90922c31655ee3ebc2_20180712104343102.jpg"
videoUrl = "https://tvetamovie.pstatic.net/libs/1203/1203262/fe6fc03524dbd8d2e499_20180706143155939.mp4-pBASE-v0-f60115-20180706143217087.mp4"

savePath = "./banner.jpg"
savePath2 = "./banner.mp4"

req.urlretrieve(imgUrl, savePath)
req.urlretrieve(videoUrl, savePath2)

print("다운로드 완료 !")
