from flask import Flask, request, jsonify
from datetime import date
from urllib.request import urlopen, Request
from urllib import parse
from bs4 import BeautifulSoup
from GBus import GBus, getBusList
from News import getNews

app = Flask(__name__)

@app.route("/keyboard")
def keyboard():
    dataSend = {
        "type": "buttons",
        "buttons": ["시작하기"]
    }
    return jsonify(dataSend)

@app.route('/message', methods=['POST'])
def Message():
    dataReceive = request.get_json()
    content = dataReceive['content']

    if content == "시작하기" or content == "도움말":
        dataSend = {
            "message": {
				"text": """[베이직 봇 사용 설명서]

안녕하세요, 베이직 봇 입니다.

<현재 지원 하는 기능>

1. 남은 복무 일 보기
명령어: 전역=전역 날짜

2. 음원 차트 TOP100 보기
명령어: 음원 + 차트

3. 미세먼지 측정기
명령어: 미세(먼지)=측정소 명
TIP: ( ) 내용은 생략가능

4. 리그오브레전드 전적 검색
명령어: 전적=소환사 이름

5. 정류장 별 버스 도착 안내
명령어: 버스=정류장 이름

6. 뉴스 기사 검색
명령어: 기사=키워드

계속해서 기능을 추가하고 있으니 수시로 도움말을 확인해주세요!
"""
            }
        }
        
    # 기능
    elif "전역=" in content:
        dataSend = {
            "message": {
                "text": getDate(content)
            }
        }
    elif ("음원" in content or "음악" in content) and "차트" in content:
        dataSend = {
            "message": {
                "text": musicChart()
            }
        }
    elif "미세먼지=" in content or "미세=" in content:
        dataSend = {
            "message": {
                "text": getPm(content)
            }
        }
    elif "전적=" in content:
        dataSend = {
            "message": {
                "text": lolSearch(content)
            }
        }
    
    # 버스 도착 안내
    elif "버스=" in content:
        stationList = GBus(content.split("=")[1])
        if len(stationList) == 0:
            dataSend = {
                "message": {
                    "text": "해당 정류장을 찾을 수 없습니다."
                }
            }
        else:
            dataSend = {
                "message": {
                    "text": "찾고자 하는 정류장을 선택해주세요."
                },
                "keyboard": {
                    "type": "buttons",
                    "buttons": stationList
                }
            }
    elif "^" in content and "-" in content and "(" in content and ")" in content:
        output = getBusList(content)
        dataSend = {
            "message": {
                "text": output
            }
        }

    # 뉴스 기사 검색기
    elif "기사=" in content:
        news = getNews(content.split("=")[1])
        if news == "":
            news = "[뉴스 기사 검색기]\n\n찾고자 하는 기사가 없습니다."
        else:
            news = "[뉴스 기사 검색기]\n\n" + news

        dataSend = {
            "message": {
                "text": news
            }
        }

    # 건의
    elif "건의" in content:
        dataSend = {
            "message": {
                "text": "건의 할 내용이 있으신가요? the_basic_@naver.com 로 건의사항을 보내주세요!"
            }
        }
    
    # 기타 채팅
    elif "ㅎㅇ" in content or "안녕" in content or "안뇽" in content:
        dataSend = {
            "message": {
                "text": "안녕하세요!  반가워요 :)"
            }
        }
    elif "ㅅㅂ" in content or "시발" in content or "씨발" in content or "개새끼" in content or "ㅂㅅ" in content or "병신" in content:
        dataSend = {
            "message": {
                "text": "힝.. 욕은 하지마세요 :("
            }
        }
    
    else:
        dataSend = {
            "message": {
                "text": "힝.. 무슨 말 인지 모르겠어요 :("
            }
        }

    return jsonify(dataSend)


# 남은 복무 일 계산기
def getDate(content):
    try:
        sp = content.split("=")[1]
        data = list(map(int, sp.split(".")))
        d0 = date.today()
        d1 = date(data[0], data[1], data[2])
        result = d1 - d0
    except IndexError:
        return "Err: 형식을 갖춰서 입력해주세요.\nExample: 전역=2020.3.24"
    except ValueError:
        return "Err: 잘못된 값이 입력되었습니다."
    else:
        return "전역까지 " + str(result.days) + "일 남으셨습니다!"


# 음원 차트 TOP100
def musicChart():
    url = "https://music.bugs.co.kr/chart"
    page = urlopen(url).read()
    soup = BeautifulSoup(page, 'html.parser')

    title = soup.select("table.list.trackList.byChart > tbody > tr th p.title")
    artist = soup.select("table.list.trackList.byChart > tbody > \
                     tr td.left p.artist")

    result = "[Bugs로 TOP100 차트 보기]\n\n"
    for idx, e in enumerate(title, 1):
        result += str(idx) + "위: " + e.find("a")['title']
        result += "- " + artist[idx - 1].find("a")['title'] + "\n\n"

    return result


# 미세먼지 측정
def getPm(content):
    API_KEY = ""
    state_name = content.split("=")[1]

    url = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?serviceKey=" + API_KEY + "&numOfRows=10&pageSize=10&pageNo=1&startPage=1&stationName=" + parse.quote(state_name) + "&dataTerm=DAILY&ver=1.3"

    page = urlopen(url).read()
    soup = BeautifulSoup(page, 'html.parser')
    try:
        pm_value = soup.find("item")
        datatime = pm_value.datatime.string
    except AttributeError:
        return "[미세먼지 측정 결과 보고]\n\n오류: 해당 측정소는 존재하지 않습니다."
    else:
        gradeDic = {"1": "좋음", "2": "보통", "3": "나쁨", "4": "매우 나쁨"}
        result = "[미세먼지 측정 결과 보고]\n\n"
        result += "지역명: " + state_name + "\n"
        result += "측정 시간: " + datatime + "\n"
        result += "현재 미세먼지 농도: " + pm_value.pm10value.string + "㎍/㎥ (" + gradeDic[pm_value.pm10grade.string] + ")\n"
        result += "현재 초미세먼지 농도: " + pm_value.pm25value.string + "㎍/㎥ (" + gradeDic[pm_value.pm25grade.string] + ")\n"
        result += "통합 대기환경 수치: " + pm_value.khaivalue.string + "㎍/㎥ (" + gradeDic[pm_value.khaigrade.string] + ")\n\n"
        result += "미세먼지 농도가 높은 날은 꼭 마스크를 착용하세요 :)"
        return result


# 롤 전적 검색
def lolSearch(content):
    summoner = content.split('=')[1]
    url = Request("http://www.op.gg/summoner/userName=" + parse.quote(summoner), headers={'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'})
    page = urlopen(url).read()
    soup = BeautifulSoup(page, 'html.parser')

    try:
        tier = soup.select("span.tierRank")[0].string # Tier
    except IndexError:
        return "[롤 전적 검색]\n\n해당 소환사를 찾을 수 없습니다."
    else:
        if (tier == "Unranked"):
            return "[롤 전적 검색]\n\n죄송합니다. 언랭은 지원하지 않습니다."
        else:
            result = "[롤 전적 검색]\n\n"
            result += "소환사 이름: " + summoner + "\n\n"

            point = soup.select("span.LeaguePoints")[0].string.strip() # Point
            ranking = soup.select('div.LadderRank > a')[0] # 랭킹

            champName = soup.select("div.ChampionBox.Ranked div.ChampionName")
            champKDA = soup.select("div.ChampionBox.Ranked div.PersonalKDA") # KDA
            champRatio = soup.select("div.ChampionBox.Ranked div.WinRatio") # 전체 승률
            champCount = soup.select("div.ChampionBox.Ranked div.Title") # 판 수

            result += "래더 랭킹: " + ranking.find("span").string + " "
            result += "" + str(ranking).split("</span>")[1].split("%")[0].strip().replace("(", "") + "%\n"

            win = soup.select("span.WinLose > span.wins")[0].string # 승
            loss = soup.select("span.WinLose > span.losses")[0].string # 패
            rate = soup.select("span.WinLose > span.winratio")[0].string # 승률

            result += "티어: " + tier + ", " + point + "\n"
            result += "승률: " + win + " " + loss + " ("+ rate + ")\n\n"

            result += "<현재 시즌 MOST 챔피언>\n\n"

            for i in range(len(champName)):
                result += "MOST " + str(i + 1) + ": " + champName[i]['title'] + "\n"
                result += "평점: " + champKDA[i].find("span").string + "\n"
                result += "승률: " + champRatio[i].string.strip() + "(" + champCount[i].string + ")\n\n"

            friends = soup.select("td.SummonerName.Cell a.Link")

            if len(friends) > 0:
                totalCell = soup.select("td.GameCount.Cell")
                winCell = soup.select("td.Win.Cell")
                loseCell = soup.select("td.Lose.Cell")
                ratioCell = soup.select("td.WinRatio.Cell")		

                result += "<최근 같이 게임한 소환사 목록>\n\n"

                for e in range(len(friends)):
                    result += "소환사: " + friends[e].string + "\n"
                    result += "전적: " + totalCell[e].string + "전 " + winCell[e].string.strip() + "승 " + loseCell[e].string.strip() + "패 (승률: " + ratioCell[e].string.strip() + ")\n\n"

            lastTotal = soup.select("div.WinRatioTitle span.total")  # 최근 20전
            lastWin = soup.select("div.WinRatioTitle span.win")  # 승
            lastLose = soup.select("div.WinRatioTitle span.lose")  # 패

            result += "======================\n"
            result += "최근 20게임 전적: " + lastTotal[0].string + "전 " + lastWin[0].string + "승 " + lastLose[0].string + "패" 
            return result


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

