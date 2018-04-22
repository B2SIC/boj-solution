class PostFix:
    def __init__(self, get_exp):
        self.STACK_SIZE = 20
        self.top = -1
        self.stack = [0] * self.STACK_SIZE
        self.get_expression = get_exp
        self.eos = self.stack[0]
        self.calc_data = ""

        # Priority ##########
        self.dic_priority = {'+': 1, '-': 1, ')': 3, '(': 0, '*': 2, '/': 2}

    ###############
    # Stack def ###
    ###############

    def is_full(self):
        if self.top == self.STACK_SIZE - 1:
            return True
        else:
            return False

    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False

    def stack_push(self, item):
        if self.is_full():
            print("Stack is full")
        else:
            self.top += 1
            self.stack[self.top] = item

    def stack_pop(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            pop_item = self.stack[self.top]
            self.top -= 1
            return pop_item

    def display_stack(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            sp = self.top

            while sp != -1:
                print(self.stack[sp])
                sp -= 1

    ##################
    # Postfix ########
    ##################
    def postfix(self):
        # Divide Expression
        for elem in self.get_expression:
            if elem.isdecimal():
                print(elem, end=' ')
                self.calc_data += elem
            elif elem == "(":
                self.stack_push(elem)
            elif elem == ")":
                while self.stack[self.top] != "(":
                    print_data = self.stack_pop()
                    print(print_data, end=' ')
                self.stack_pop()
                self.calc_data += print_data
            else:
                # 연산자가 1개만 들어올 경우, 즉 스택이 비어있을 경우에 대한 예외처리 코드 영역
                if self.top == -1:
                    self.stack_push(elem)
                else:
                    if self.dic_priority[self.stack[self.top]] < self.dic_priority[elem]:
                        self.stack_push(elem)
                    else:
                        print_data = self.stack_pop()
                        print(print_data, end=' ')
                        self.stack_push(elem)
                        self.calc_data += print_data

        while True:
            if self.is_empty():
                break
            else:
                token = self.stack_pop()

                if token != self.eos:
                    print(token, end=' ')
                    self.calc_data += token
        print()

    ##################
    # Calc_postfix ###
    ##################
    def calc_postfix(self):
        for token in self.calc_data:
            if token.isdecimal():
                self.stack_push(token)
            else:
                apply_1 = str(self.stack_pop())
                apply_2 = str(self.stack_pop())
                result = apply_2 + token + apply_1
                self.stack_push(eval(result))
        print(self.stack_pop())


if __name__ == "__main__":
    p1 = PostFix("3+4")
    p1.postfix()
    p1.calc_postfix()
    p2 = PostFix("7*8-(2+3)")
    p2.postfix()
    p2.calc_postfix()
    p3 = PostFix("7*(2+3)*8")
    p3.postfix()
    p3.calc_postfix()
