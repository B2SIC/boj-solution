import requests
import json

s = requests.Session()

r = s.get('http://httpbin.org/stream/20', stream=True)
# print(r.text)
# print(r.json())
# print(r.encoding)

if r.encoding is None:
    r.encoding = "utf-8"

for line in r.iter_lines(decode_unicode=True):
    # print(line)
    j = json.loads(line)
    # print(type(j))
    print(j['origin'])  # dict

    for e in j.keys():
        print("key:", e, " values:", j[e])
