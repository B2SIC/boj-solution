class Palindrome:
    def __init__(self, s):
        self.judgeString = s
        self.tables = []
        self.lengths = []

        self.create_table()

    def is_palindrome(self, s):
        if s == "".join(reversed(s)):
            return True
        else:
            return False

    def create_table(self):
        for i in range(len(self.judgeString) + 1):
            for j in range(len(self.judgeString) + 1):
                if self.judgeString[i:j] != "":
                    self.tables.append(self.judgeString[i:j])

    def get_max_length(self):
        for elem in self.tables:
            if self.is_palindrome(elem):
                self.lengths.append(len(elem))

        return max(self.lengths)


str_input = input("Input your string: ")
pal = Palindrome(str_input)
print(pal.get_max_length())
