def solution(dict_repr, key, cut):
    scores = eval(dict_repr)
    re_list = []
    for i in scores.keys():
        if scores[i][key] >= cut:
            re_list.append(i)
    return sorted(re_list)

print(solution("{'Mary': {'Korean': 80, 'Math': 65, 'English': 58}, "
               "'Peter': {'Korean': 60, 'Math': 95, 'English': 72},"
               "'John': {'Korean': 70, 'Math': 78, 'English': 69}}", "Korean", 70))