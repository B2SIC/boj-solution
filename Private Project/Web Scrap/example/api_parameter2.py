import urllib.request as ur
from urllib.parse import urlencode

API = "http://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp"

values = {
    'ctxCd' : '1012'
}

print('before', values)

params = urlencode(values)
print('after', params)

url = API + "?" + params
print("요청 url", url)

reqData = ur.urlopen(url).read().decode('utf-8')
print("출력: ", reqData)