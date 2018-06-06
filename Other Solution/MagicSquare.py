class Square:
    def __init__(self, square):
        self.square = square
        self.sum = 0

    def is_magic_square(self):
        # 기준 값 설정 (첫 번째 행의 합을 구해서 self.sum 에 저장)
        square_sum = 0
        for i in range(1):
            for j in range(len(self.square)):
                square_sum += self.square[i][j]

        self.sum = str(square_sum)

        # 행의 값들이 모두 같은지 판단
        for i in range(len(self.square)):
            tmp_sum = 0
            for j in range(len(self.square)):
                tmp_sum += self.square[i][j]

            if tmp_sum != square_sum:
                return False

        # 열의 값들이 모두 같은지 판단
        for i in range(len(self.square)):
            tmp_sum = 0
            for j in range(len(self.square)):
                tmp_sum += self.square[j][i]

            if tmp_sum != square_sum:
                return False

        # 대각선의 값들이 모두 같은지 판단 (오른쪽 진행)
        tmp_sum = 0

        for i in range(len(self.square)):
            tmp_sum += self.square[i][i]

        if tmp_sum != square_sum:
            return False

        # 대각선의 값들이 모두 같은지 판단 (왼쪽 진행)
        tmp_sum = 0
        for i in range(len(self.square)):
            tmp_sum += self.square[i][len(self.square) - 1 - i]

        if tmp_sum != square_sum:
            return False

        # return False 가 아니라면 행, 열, 대각선의 합이 모두 같다는 의미이므로 True 반환
        return True

    def get_sum(self):
        return self.sum

# 1 1 1 1
# 1 1 1 1
# 1 1 1 1
# 1 1 1 1
sq = Square([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]])
print(sq.is_magic_square())

# 1 1 2
# 1 1 2
# 1 1 2
sq2 = Square([[1, 1, 2], [1, 1, 2], [1, 1, 2]])
print(sq2.is_magic_square())
