import pytube
import os
import subprocess
from bs4 import BeautifulSoup
from urllib.request import urlopen

class Youtube:
    def __init__(self):
        self.downList = []
        self.down_dir = "/home/user/Play_With_Python/Private Project/Web Scrap/Youtube Downloader/MP3"

    def downloader(self, url, settings=0):
        self.yt = pytube.YouTube(url)
        self.videos = self.yt.streams.all()

        # 화질 리스트 출력
        for idx in range(len(self.videos)):
            print(idx, ': ', self.videos[idx])

        self.cNum = int(input("다운 받을 화질을 선택하세요: "))

        self.videos[self.cNum].download(self.down_dir)

        print(self.yt.title + ": 다운로드 완료")

        if settings:
            self.converter(self.yt.title)

    def multi_downloader(self, settings=0):
        print("SYSTEM: 멀티 다운로더는 기본 화질이 0번으로 설정 됩니다.")
        f = open("/home/user/Play_With_Python/Private Project/Web Scrap/Youtube Downloader/down_list.txt", 'r')
        for line in f:
            self.downList.append(line)

        for multi_url in self.downList:
            self.yt = pytube.YouTube(multi_url)
            self.videos = self.yt.streams.all()
            self.cNum = 0
            self.videos[self.cNum].download(self.down_dir)

            print(self.yt.title + " : 다운로드 완료")

            if settings:
                self.converter(self.yt.title)

    def converter(self, title):
        newFileName = title.replace("/", "") + ".mp3"
        oriFileName = self.videos[self.cNum].default_filename

        subprocess.call(['ffmpeg', '-i',
                         os.path.join(self.down_dir, oriFileName),
                         os.path.join(self.down_dir, newFileName)])

        print("########################################")
        print("SYSTEM : MP3 변환 작업을 마쳤습니다.")
        print("########################################")

print("########################################")
print("########## YOUTUBE DOWNLOADER ##########")

while True:
    print("########################################")
    print("1 : Youtube 싱글 다운로더")
    print("2 : Youtube 싱글 다운로더 (+ MP3 변환)")
    print("3 : Youtube 멀티 다운로더")
    print("4 : Youtube 멀티 다운로더 (+ MP3 변환)")
    print("5 : Youtube 재생 목록으로부터 링크 가져오기")
    print("9 : 프로그램 종료")
    print("########################################\n")

    command = int(input("작업 번호를 선택해주세요: "))

    if command == 1 or command == 2:
        youtubeUrl = input("Youtube 동영상 주소를 입력하세요: ")
        worker = Youtube()

        if command == 1:
            worker.downloader(youtubeUrl)
        else:
            worker.downloader(youtubeUrl, 1)
    elif command == 3 or command == 4:
        multi_worker = Youtube()

        if command == 3:
            multi_worker.multi_downloader()
        else:
            multi_worker.multi_downloader(1)
    elif command == 5:
        print("########################################")
        print("경고 : 작업 결과는 기존 down_list.txt 파일에 덮어씌워집니다.")
        print("########################################")
        url = input("재생목록에 들어있는 동영상 주소를 입력하세요: ")

        page = urlopen(url).read()

        soup = BeautifulSoup(page, 'lxml')

        getUrl = soup.select(".spf-link.playlist-video.clearfix.yt-uix-sessionlink.spf-link")

        with open("down_list.txt", "w") as f:
            for elem in getUrl:
                f.write("http://youtube.com" + elem.get("href") + "\n")

        print("########################################")
        print("SYSTEM : 작업 완료")
    elif command == 9:
        print("SYSTEM : Bye Bye !")
        break
