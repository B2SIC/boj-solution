def sum_n(n):
    result = 0
    for i in range(1, n + 1):
        result += i
    return result


def sum_formula(n):
    return n * (n + 1) // 2


def square_n(n):
    result = 1
    for i in range(1, n + 1):
        result += i * i
    return result


def square_formula(n):
    return n * (n + 1) * (2 * n + 1) // 6


print(sum_n(100))
print(sum_formula(100))
print(square_n(10))
print(square_formula(10))


