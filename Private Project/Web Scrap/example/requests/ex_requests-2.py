import requests

# Response Status Code

s = requests.Session()
r = s.get("http://httpbin.org/get")

print(r.status_code)  # 200, 404, 403 ...
print(r.ok)

# json 테스트 사이트
# https://jsonplaceholder.typicode.com

r = s.get('https://jsonplaceholder.typicode.com/posts/1')
print(r.text)
print(r.json().keys())
print(r.json().values())
print(r.encoding)
print(r.content)
print(r.raw)
