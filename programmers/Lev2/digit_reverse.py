def digit_reverse(n):
    rev_n = reversed(str(n))
    result = []

    for i in rev_n:
        result.append(int(i))
    return result

print(digit_reverse(12345))