def solution(list_repr, key):
    re_list = []
    my_list = eval(list_repr)

    for j in range(len(my_list)):
        if my_list[j].get(key, 0) == 0:
            return []

    tmp_list = sorted(my_list, key = lambda dic:dic[key])
    for i in range(len(my_list)):
        re_list.append(tmp_list[i]['name'])

    return re_list

get_list = "[{'name': 'John', 'height': 166, 'weight': 65}, {'name': 'Frank', 'height': 168, 'weight': 72}, {'name': 'Hoon', 'height': 190, 'weight': 72}]"
print(solution(get_list, "height"))