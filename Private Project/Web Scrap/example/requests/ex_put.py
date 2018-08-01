import requests
import json

# REST : POST, GET, PUT: UPDATE, REPLACE (FETCH: UPDATE, MODIFY), DELETE

payload1 = {'key1': 'value1', 'key2': 'value2'}  # 데이터를 서버상에 Request 할 때 담을 수 있는 것 (payload) #dict
payload2 = (('key1', 'value1'), ('key2', 'value2')) # tuple
payload3 = {'sone': 'nice'}

# r = requests.put('http://httpbin.org/put', data=payload1)
# print(r.text)

# r = requests.put('https://jsonplaceholder.typicode.com/posts/1', data=payload1)
# print(r.text)

r = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
print(r.text)
