import urllib.request
import bs4
import plivo
import time

def goal(nation):
    client = plivo.RestClient(auth_id='YOUR_AUTH_ID', auth_token='YOUR_AUTH_TOKEN')

    response = client.messages.create(
        src = '1111111111',
        dst = 'PHONE_NUMBER', # KOREA: +8210..
        text = time.strftime('%H' + '시' + ' %M' + '분' + ' %S' + '초 ') + nation + " Goal !! "
    )
    print(response)

# init settings
url = 'https://search.naver.com/search.naver?where=nexearch&query=%EB%B2%A8%EA%B8%B0%EC%97%90+%EC%9E%89%EA%B8%80%EB%9E%9C%EB%93%9C&sm=top_lve&ie=utf8'
data = urllib.request.urlopen(url).read()
soup = bs4.BeautifulSoup(data, 'lxml')
score = soup.select('.score > span')
nation = soup.select('.nation_name')

team1_score = score[0].getText()
team2_score = score[1].getText()

while True:
    data = urllib.request.urlopen(url).read()
    soup = bs4.BeautifulSoup(data, 'lxml')
    score = soup.select('.score > span')
    nation = soup.select('.nation_name')

    team1 = score[0]
    team2 = score[1]

    nation1 = nation[0]
    nation2 = nation[1]

    print(time.strftime('%H' + '시' + ' %M' + '분' + ' %S' + '초 '))
    print("매치: " + nation1.getText() + " vs " + nation2.getText())
    print("스코어: " + team1.getText() + " : " + team2.getText())
    print()

    if team1_score != team1.getText():
        print("기존 스코어: " + team1_score + " 갱신된 스코어: " + team1.getText())
        goal(nation1.getText())
        team1_score = team1.getText()
    elif team2_score != team2.getText():
        print("기존 스코어: " + team2_score + "갱신된 스코어: " + team2.getText())
        goal(nation2.getText())
        team2_score = team2.getText()

    time.sleep(30)
