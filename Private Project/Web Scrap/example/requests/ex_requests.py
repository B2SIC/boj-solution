import requests

s = requests.Session()
# r = s.get("https://www.naver.com")  #PUT(FETCH), DELETE, GET, POST
# print('1', r.text)

# Cookie
# r = s.get('http://httpbin.org/cookies', cookies={'from': 'myName'})
# print(r.text)

# Headers
# url = 'http://httpbin.org/get'
# headers = {"user-agent": "myPythonApp_1.0.0"}
#
# r = s.get(url, headers=headers)
# print(r.text)

s.close()

# with 문 사용 가능
with requests.Session() as s:
    r = s.get("https://www.naver.com")
    print(r.text)
