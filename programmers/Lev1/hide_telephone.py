def hide_numbers(s):
    length = len(s)
    count = 0
    result = ""
    for i in s:
        if count == length - 4:
            result += i
        else:
            result += "*"
            count += 1
    return result


def hide_numbers_p(s):
    return '*'*len(s[:-4]) + s[-4:]

print(hide_numbers("01012345678"))
print(hide_numbers_p("010125678"))