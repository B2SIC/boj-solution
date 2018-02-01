from pprint import pprint
import array
# pprint(pretty print) : 자료 구조를 사람이 보기 좋게 출력해주는 모듈.

data = [(1, {"a": "가", "b": "나", "c": "다", "d": "라"}),
        (2, {"e": "마", "f": "바", "g": "사", "h": "아"})
        ]

# pprint 모듈에 pprint() 함수를 이용하여 자료구조를 출력해보기
print(data)
pprint(data)

# array: 동일한 자료형만 사용할 수 있다.
# 리스트는 서로 다른 자료형을 모두 사용할 수 있다는 점에서 array 와 차이점이 있다.
# 메모리 활용 측면에서 리스트보다 효율적이다. (한 가지 형태의 자료형만 다루기 때문)
# 시퀀스 자료 구조를 정의하는데, 리스트와의 차이점은 모든 자료형이 동일하다는 점.

str = "aabcdefgh"

# array(타입 코드, 타입에 대한 값), u = 유니코드
arr = array.array("u", str)
print(arr)

# 타입코드: https://docs.python.org/3/library/array.html
print(array.typecodes)

# range(5) => 0 ~ 4
arr1 = array.array("i", range(5))
print(arr1)

arr1.extend(range(5))
print(arr1)

# Slice
print(arr1[3:6])

print(list(enumerate(arr1)))
