def number_generator(x, n):
    result = []
    for i in range(x, (x * n) + 1, x):
        result.append(i)
    return result

print(number_generator(3, 5))