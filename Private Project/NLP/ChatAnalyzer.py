# 모듈 설치 : https://konlpy-ko.readthedocs.io/ko/v0.4.4/install/#
# 참고: http://www.konlpy.org/ko/v0.4.4/api/konlpy.tag/#mecab-class

from konlpy.tag import Mecab
from pprint import pprint

mecab = Mecab()

getFileName = input("텍스트 파일 이름을 입력해주세요: ")

# Default Value
if getFileName == "":
    getFileName = "KakaoTalkChats.txt"

with open(getFileName, 'r') as f:
    chatLog = f.readlines()

NLPData = []
wordDic = {}

# Get Chat Content
for i in range(len(chatLog)):
    NLPData.append(chatLog[i].split(":")[-1])

# Processing
for k in range(len(NLPData)):
    wordList = mecab.morphs(NLPData[k])

    # Dictionary Count
    for j in range(len(wordList)):
        wordDic[wordList[j]] = wordDic.get(wordList[j], 0) + 1

# Save DataFile
with open("chatLog.txt", 'w') as f:
    f.write("채팅방 이름: " + chatLog[0])
    sortedDic = sorted(wordDic.items(), key=lambda k: k[1], reverse=True)

    for i in range(len(sortedDic)):
        data = sortedDic[i][0] + " : " + str(sortedDic[i][1]) + "\n"
        f.write(data)
