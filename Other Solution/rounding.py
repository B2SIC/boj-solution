def solution(n, p):
    str_n = str(n)
    num_list = [int(i) for i in str_n]
    num_list.reverse()

    if len(str_n) == p:
        result = ''
        if num_list[-1] >= 5:
            result += '1' + '0' * len(str_n)
            return int(result)
    elif len(str_n) < p:
        return 0
    elif p <= 0:
        return n

    if num_list[p - 1] >= 5:
        num_list[p] += 1
        for i in range(p):
            num_list[i] = 0
    else:
        for i in range(p):
            num_list[i] = 0

    num_list.reverse()
    answer = ''
    for i in num_list:
        answer += str(i)
