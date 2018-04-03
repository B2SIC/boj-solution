def is_full():  # Check stack is full?
    global top, stackSize  # 전역 변수로서의 top 사용
    if top == stackSize - 1:
        return 1
    else:
        return 0


def is_empty():  # Check stack is empty?
    global top
    if top == -1:
        return 1
    else:
        return 0


def push(data):  # Push the data in stack
    global top, stack
    top += 1
    try:
        stack[top] = data
    except IndexError:
        print("Err: Maybe Stack is Full")


def pop():  # Pop the data
    global top, stack
    try:
        result = stack[top]
        top -= 1
        return result
    except IndexError:
        print("Err : Maybe Stack is Empty")


def display_stack():  # Print stack
    global top, stack

    if is_empty():
        print("Stack is empty!")
    else:
        sp = top

        while sp != -1:
            print(stack[sp])
            sp -= 1

def display_stack_reverse(row, col):
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
