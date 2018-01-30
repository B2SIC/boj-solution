# Collections Counter
# 컨테이너에 동일한 값의 자료가 몇 개인지를 파악하는데 사용하는 객체

import collections

print(collections.Counter(['aa', 'cc', 'dd', 'aa', 'bb', 'ee']))
print(collections.Counter({"가":3, "나":2, "다":4}))
print(collections.Counter(a=2, b=4, c=1))

container = collections.Counter()
print(container)

container.update("aabcdeffgg")
print(container)

container.update({'c':2, 'f':3})
print(container)

# Counter 객체의 접근

print(container['f'])

for n in "abdfeh":
    print("%s: %d" % (n, container[n]))

ct = collections.Counter("Hello jenny")
ct['x'] = 0

print(ct)

print(list(ct.elements()))

# most_common(n) 사용하기
# 상위 n개를 시퀀스로 만든다.

ct2 = collections.Counter()
with open('test.txt', 'rt') as f:
    for li in f:
        ct2.update(li.rstrip().lower())

for item, cnt in ct2.most_common(5):
    print("%s : %2d" % (item, cnt))

print(ct2.most_common())
