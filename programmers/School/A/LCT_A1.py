def solution(num_list):
    re_list = []
    t_list = sorted(num_list)
    re_list.append(t_list[-1])
    re_list.append(num_list.index(t_list[-1]))
    return re_list

print(solution([3, 29, 38, 12, 57, 74, 40, 85, 61]))