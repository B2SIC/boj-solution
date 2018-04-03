# 함수 동작 설명: Hw1.py 파일 주석 참고

def is_full():  # 스택이 가득 찼는지 체크한다.
    global top, stackSize  # 전역 변수로서의 top 사용
    if top == stackSize - 1:
        return 1
    else:
        return 0


def is_empty():  # 스택이 비었는지 체크한다.
    global top
    if top == -1:
        return 1
    else:
        return 0


def push(data):  # 데이터를 스택에 저장한다.
    global top, stack
    top += 1
    try:
        stack[top] = data
    except IndexError:
        print("Err: Maybe Stack is Full")


def pop():  # 마지막으로 저장된 데이터를 스택에서 꺼낸다.
    global top, stack
    try:
        result = stack[top]
        top -= 1
        return result
    except IndexError:
        print("Err : Maybe Stack is Empty")


def display_stack():  # 스택을 최근 저장된 순서대로 출력한다.
    global top, stack

    if is_empty():
        print("Stack is empty!")
    else:
        sp = top

        while sp != -1:
            print(stack[sp])
            sp -= 1

def display_stack_reverse(row, col):  # 스택을 아래서 부터 출력한다.
    global top, stack

    if is_empty():
        print("Stack is empty!")
    else:
        sp = 0

        while sp != top + 1:
            print(stack[sp], end=" -> ")
            sp += 1

        print([row, col])

top = -1
stackSize = 100
stack = [0] * stackSize
