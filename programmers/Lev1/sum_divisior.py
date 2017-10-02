def sumDivisor(num):
    divide_list = []

    for i in range(1, num + 1):
        if num % i == 0:
            divide_list.append(i)

    return sum(divide_list)

print(sumDivisor(30))