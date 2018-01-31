# namedtuple()
# 일반 튜플 방식에서는 필드가 많을 경우 각각의 순서가 어떠한 의미를 내포하는지 헷갈릴 수 있다.
# 따라서 이러한 필드에 이름을 지정해서 사용할 경우 이러한 문제를 방지할 수 있다.
# 사전을 사용할 수도 있지않을까? => 메모리를 좀 더 많이 사용하게된다.
# 이러한 부담을 줄일 수 있는 방법이 namedtuple 이다.

import collections

aa = ("홍길동", 24, "남")
print(aa)

bb = ("강복녀", 21, "여")
print(bb[0])

for n in [aa, bb]:
    print("%s 은(는) %d세의 %s성 입니다." % n)

# namedtuple 의 사용
Person = collections.namedtuple("Person", "name age gender")

aa = Person(name = "강길동", age = 25, gender = "남")
bb = Person(name = "강복녀", age = 21, gender = "여")

for i in [aa, bb]:
    print("%s 은(는) %d세의 %s성 입니다." % i)

print()
# OrderedDict : 자료의 순서를 기억하는 사전형 클래스
# 입력한 순서를 그대로 기억하고 있다.
# 그렇다면 파이썬에서 표준으로 제공하는 딕셔너리와 차이점은?
# => 표준 딕셔너리는 순서를 기억하지않지만 OrderedDict 는 순서를 기억한다.

dic = {}
dic["서울"] = "LG 트윈스"
dic["대구"] = "삼성 라이온즈"
dic["광주"] = "기아 타이거즈"

for i, j in dic.items():
    print(i, j)

print("==================")

dic1 = collections.OrderedDict()
dic1["서울"] = "LG 트윈스"
dic1["대구"] = "삼성 라이온즈"
dic1["광주"] = "기아 타이거즈"

for i, j in dic1.items():
    print(i, j)

print("< 비교를 이용한 표준 사전과 OrderedDict 의 차이점 >")

dic3 = {}
dic3["서울"] = "LG 트윈스"
dic3["대구"] = "삼성 라이온즈"
dic3["광주"] = "기아 타이거즈"

dic4 = {}
dic4["서울"] = "LG 트윈스"
dic4["광주"] = "기아 타이거즈"
dic4["대구"] = "삼성 라이온즈"

# 순서가 다름에도 True 값을 반환한다.
print(dic3 == dic4)

dic5 = collections.OrderedDict()
dic5["서울"] = "LG 트윈스"
dic5["대구"] = "삼성 라이온즈"
dic5["광주"] = "기아 타이거즈"

dic6 = collections.OrderedDict()
dic6["서울"] = "LG 트윈스"
dic6["광주"] = "기아 타이거즈"
dic6["대구"] = "삼성 라이온즈"

# OrderedDict 는 순서를 중요시 하기 때문에 순서가 다르면 False 값을 반환한다.
print(dic5 == dic6)
