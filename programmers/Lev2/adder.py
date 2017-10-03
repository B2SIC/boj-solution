def adder(a, b):
    result = 0
    for i in range(min(a,b), max(a,b) + 1):
        result += i
    return result

print(adder(5, 5))
print(adder(3, 5))
print(adder(96, 12))