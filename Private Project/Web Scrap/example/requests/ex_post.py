import requests
import json

# r = requests.get('https://api.github.com/events')
# r.raise_for_status() # 에러가 발생했을 때 raise 호출 (에러 파악 가능)
# print(r.text)

jar = requests.cookies.RequestsCookieJar()
jar.set('name', 'kim', domain="httpbin.org", path='/cookies')

# r = requests.get("http://httpbin.org/cookies", cookies=jar)
# r.raise_for_status()
# print(r.text)

# r = requests.get('https://github.com', timeout=3)  # 서버가 반응할 때까지 5초간 대기하곘다.
# print(r.text)

# r = requests.post("http://httpbin.org/post", data={'name': 'kim'}, cookies=jar)
# print(r.text)

payload1 = {'key1': 'value1', 'key2': 'value2'}  # 데이터를 서버상에 Request 할 때 담을 수 있는 것 (payload) #dict
payload2 = (('key1', 'value1'), ('key2', 'value2')) # tuple
payload3 = {'sone': 'nice'}

# r = requests.post("http://httpbin.org/post", data=payload2) # form
# print(r.text)

r = requests.post("http://httpbin.org/post", data=json.dumps(payload3)) # json
print(r.text)
