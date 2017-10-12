def solution(str_list):
    dic_list = {}

    for i in str_list:
        dic_list[i] = dic_list.get(i, 0) + 1
    dic_list = sorted(dic_list.items(), key=lambda dic: dic[1], reverse=True)

    return dic_list[0][0]

print(solution(['kook', 'min', 'kook', 'university', 'kook']))
print(solution(['1', '1', '1', 'a', 'a']))