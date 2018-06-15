import random


class Updown:
    def __init__(self, limit):
        self.secret_number = random.randint(1, limit)
        self.answer = ""
        self.tries = 0

    def check_number(self, get_number):
        self.tries += 1

        if get_number == self.secret_number:
            self.answer = "Success"
            return True
        elif get_number > self.secret_number:
            self.answer = "Smaller than your number"
            return False
        elif get_number < self.secret_number:
            self.answer = "Greater than your number"
            return False

    def game_start(self):
        print("Ok.. New Game Start !")
        while True:
            input_number = int(input("What is your guess? : "))
            answer = self.check_number(input_number)
            if answer is True:
                break
            else:
                print("Sry..", self.answer)

        print("Success in %d trials" % self.tries)


get_limit = int(input("Input limit number: "))
game1 = Updown(get_limit)
game1.game_start()
