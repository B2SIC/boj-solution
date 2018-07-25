# for GUI Settings
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QImage
from PyQt5 import uic

# for URL Encoding
from urllib.parse import quote

# for Parsing Data
import urllib
import urllib.request
import bs4

form_class = uic.loadUiType("pylol.ui")[0]


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.move_center()
        self.pushButton.clicked.connect(self.get_data)
        self.lineEdit.returnPressed.connect(self.get_data)

    def move_center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def get_data(self):
        try:
            userName = self.lineEdit.text()

            url = 'http://www.op.gg/summoner/spectator/userName=' + quote(userName)
            data = urllib.request.urlopen(url).read()
            soup = bs4.BeautifulSoup(data, 'html.parser')

            # Get Summoner ID
            select = soup.select('.Button.SemiRound.Blue')
            userId = select[0].get('onclick').split("'")[1]
            playingChampion = soup.select('#SpectateBigListRow-' + userId + ' .Image.tip')[0].get('href').split('/')[2]
            self.label_champion.setText(playingChampion.capitalize())

        except IndexError:
            QMessageBox.critical(self, "Try Again..", "This summoner is not playing the game :<")

        else:
            posDic = {"Change": "/",
                      "Top": "/top",
                      "Mid": "/mid",
                      "Jungle": "/jungle",
                      "Ad": "/adc",
                      "Support": "/support"}

            data_url = 'http://www.op.gg/champion/' + playingChampion + '/statistics' \
                       + posDic[self.comboBox.currentText()]
            data_soup = bs4.BeautifulSoup(urllib.request.urlopen(data_url).read(), 'html.parser')

            img_data = data_soup.select('.champion-stats__list__item.tip img')
            skill_name = data_soup.select('.champion-stats__list__item.tip span')

            try:
                recommend_img_data = data_soup.select('.champion-overview__row.champion-overview__row--first')
                recommend_img_data = recommend_img_data[1].select('.champion-stats__list__item.tip img')

                recommend_img_data2 = data_soup.select('.champion-overview__row')
                recommend_img_data2_1 = recommend_img_data2[3].select('.champion-stats__list__item.tip img')
                recommend_img_data2_2 = recommend_img_data2[4].select('.champion-stats__list__item.tip img')
                recommend_img_data2_3 = recommend_img_data2[5].select('.champion-stats__list__item.tip img')

                self.label_skill_name_1.setText(skill_name[0].getText())
                self.label_skill_name_2.setText(skill_name[1].getText())
                self.label_skill_name_3.setText(skill_name[2].getText())

                # ========= Get Image Url =========
                skill_1 = "http:" + img_data[0].get('src')
                skill_2 = "http:" + img_data[1].get('src')
                skill_3 = "http:" + img_data[2].get('src')

                item_1 = "http:" + recommend_img_data[0].get('src')
                item_2 = "http:" + recommend_img_data[1].get('src')
                item_3 = "http:" + recommend_img_data[2].get('src')

                item_4 = "http:" + recommend_img_data2_1[0].get('src')
                item_5 = "http:" + recommend_img_data2_1[1].get('src')
                item_6 = "http:" + recommend_img_data2_1[2].get('src')

                item_7 = "http:" + recommend_img_data2_2[0].get('src')
                item_8 = "http:" + recommend_img_data2_2[1].get('src')
                item_9 = "http:" + recommend_img_data2_2[2].get('src')

                item_10 = "http:" + recommend_img_data2_3[0].get('src')
                item_11 = "http:" + recommend_img_data2_3[1].get('src')
                item_12 = "http:" + recommend_img_data2_3[2].get('src')

            except IndexError:
                QMessageBox.critical(self, "Try Again..", "Insufficient data :<")

            else:
                # ========== Display Image files ===========
                image = QImage()
                image.loadFromData(urllib.request.urlopen(skill_1).read())
                self.label_skill_1.setPixmap(QPixmap(image))

                image.loadFromData(urllib.request.urlopen(skill_2).read())
                self.label_skill_2.setPixmap(QPixmap(image))

                image.loadFromData(urllib.request.urlopen(skill_3).read())
                self.label_skill_3.setPixmap(QPixmap(image))

                image.loadFromData(urllib.request.urlopen(item_1).read())
                self.label_item_1.setPixmap(QPixmap(image))

                image.loadFromData(urllib.request.urlopen(item_2).read())
                self.label_item_2.setPixmap(QPixmap(image))

                image.loadFromData(urllib.request.urlopen(item_3).read())
                self.label_item_3.setPixmap(QPixmap(image))

                image.loadFromData(urllib.request.urlopen(item_4).read())
                self.label_item_4.setPixmap(QPixmap(image))

                image.loadFromData(urllib.request.urlopen(item_5).read())
                self.label_item_5.setPixmap(QPixmap(image))

                image.loadFromData(urllib.request.urlopen(item_6).read())
                self.label_item_6.setPixmap(QPixmap(image))

                image.loadFromData(urllib.request.urlopen(item_7).read())
                self.label_item_7.setPixmap(QPixmap(image))

                image.loadFromData(urllib.request.urlopen(item_8).read())
                self.label_item_8.setPixmap(QPixmap(image))

                image.loadFromData(urllib.request.urlopen(item_9).read())
                self.label_item_9.setPixmap(QPixmap(image))

                image.loadFromData(urllib.request.urlopen(item_10).read())
                self.label_item_10.setPixmap(QPixmap(image))

                image.loadFromData(urllib.request.urlopen(item_11).read())
                self.label_item_11.setPixmap(QPixmap(image))

                image.loadFromData(urllib.request.urlopen(item_12).read())
                self.label_item_12.setPixmap(QPixmap(image))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
