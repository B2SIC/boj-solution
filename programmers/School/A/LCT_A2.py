def solution(string_list, x):
    re_string = ""
    for i in range(len(string_list)):
        if x % 2 == 0: # x가 짝수 일 때
            if i % 2 == 0: # i가 짝수 일 때
                re_string += string_list[i].upper()
            else: #i가 홀수일 때
                re_string += string_list[i].lower()
        else: # x가 홀수 일 때
            if i % 2 == 0: # i가 짝수 일때
                re_string += string_list[i].lower()
            else:
                re_string += string_list[i].upper()
    return re_string

print(solution(["aBc", "De", "xy", "fGhi"], 31))