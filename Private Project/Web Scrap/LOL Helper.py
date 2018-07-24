import sys
from PyQt5.QtWidgets import *
# URL Encoding 를 위한 urllib.parse 참조
from urllib.parse import quote
import urllib.request, bs4

app = QApplication(sys.argv)
label = QLabel("Hello PyQt")
label.show()
app.exec_()

userName = input("롤 닉네임을 입력해주세요: ")

url = 'http://www.op.gg/summoner/spectator/userName=' + quote(userName)
data = urllib.request.urlopen(url).read()
soup = bs4.BeautifulSoup(data, 'html.parser')

# Get Summoner ID
select = soup.select('.Button.SemiRound.Blue')
userId = select[0].get('onclick').split("'")[1]
playingChampion = soup.select('#SpectateBigListRow-' + userId + ' .Image.tip')[0].get('href').split('/')[2]

print(userId)
print(playingChampion)
