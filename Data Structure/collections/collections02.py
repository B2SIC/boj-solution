import collections

# Counter 객체는 산술/집합 연산이 가능하다.

ct3 = collections.Counter(['a', 'b', 'c', 'b', 'd', 'a'])
ct4 = collections.Counter('aeroplane')

print(ct3)
print(ct4)

# 더하기
print(ct3 + ct4)

# 차집합
print(ct3 - ct4)

# 교집합
print(ct3 & ct4)

# 합집합 (아이템의 최댓값만을 표시함)
print("union", ct3 | ct4)

# defaultdict : 컨테이너를 초기화 할 때 default 값을 지정한다.

def default_aa():
    return "aa"

dic = collections.defaultdict(default_aa, n1 = "hi")
print(dic)
print(dic['n1'])
# 존재하지않는 키 값이 들어갈 경우 함수를 호출한다.
print(dic['n2'])
