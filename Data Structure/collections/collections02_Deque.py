import collections

'''
 Deque : 양방향 큐(데크, 디큐)
 컨테이너 양쪽(앞뒤)에 아이템을 넣거나 뺄 수 있다.
 큐에 대한 불편함을 해결할 수 있다. (양방향 지원 가능)
 
 < 큐와 스택의 개념 >
 Queue 구조 : 한 쪽 방향으로만 넣고 그와 다른(반대) 방향으로만 뺼 수 있는 방식.
 A -------------- B
 A가 입구, B가 출구 일 때
 1이라는 값을 넣고 2라는 값을 넣으면, 1이 먼저 나오고 2가 나중에 나옴.
 
 Stack 구조 : 데이터를 넣을 때와 뺄 때 방향이 같다. (입구와 출구가 같다)
 |4|
 |3|
 |2|
 |1|
 |_|
 입구를 통해서 들어오고 입구를 통해서 다시 데이터를 뺀다.
 먼저 들어간 1은 맨 나중에 뺄 수 있다.
'''

deq = collections.deque("Hello python")
print(deq)
print(len(deq))
print(deq[0])
print(deq[-1])

deq.remove('o')
print(deq)

# 양쪽에 데이터 추가
deq.append('k')
print(deq)

deq.appendleft('k')
print(deq)

deq.extendleft('d')
print(deq)

# extend 초기화
deq1 = collections.deque()
deq1.extend("가나다라마바사")
print(deq1)

deq1.append("자")
print(deq1)

deq1.extendleft("사")
print(deq1)

# 아이템 꺼내기
'''
print("오른쪽에서부터 꺼내오기")
while True:
    try:
        print(deq1.pop(), end=' ')
    except IndexError:
        break
print()
'''
print("왼쪽에서부터 꺼내오기")
while True:
    try:
        print(deq1.popleft(), end=' ')
    except IndexError:
        break
