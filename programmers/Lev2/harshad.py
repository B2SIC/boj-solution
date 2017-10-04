def Harshad(n):
    str_n = str(n)
    sum_n = 0

    for i in str_n:
        sum_n += int(i)

    if n % sum_n == 0:
        return True
    else:
        return False

print(Harshad(18))