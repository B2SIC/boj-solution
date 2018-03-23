def solution(num_list):
    re_list = []
    result = 1
    idx = 0

    for _ in range(len(num_list)):
        tmp = num_list[idx]
        del num_list[idx]

        for i in num_list:
            result *= i

        re_list.append(result)
        num_list.append(tmp)
        result = 1
    return re_list


print(solution([1,2,3,4]))