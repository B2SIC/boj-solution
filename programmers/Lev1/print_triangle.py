def printTriangle(num):
    s = ''
    for i in range(1, num + 1):
        s += "*" * i + "\n"
    return s

print(printTriangle(5))