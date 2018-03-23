import string


def convert_to_number(s_number):
    sum = 0

    for i in s_number:
        i = int(i) + 1
        sum += i
    return sum

s = input()

'''
< 알파벳을 번호에 매칭 >
ABC : 2, DEF : 3, GHI : 4
JKL : 5, MNO : 6, PQRS : 7
TUV : 8, WXYZ : 9
'''
s_number = ""
chr_list = [x for x in string.ascii_uppercase]
code_dic = {}
count = 0
value = 2

for chr in chr_list:
    # 'S', 'Z' 예외 처리
    if chr == 'S':
        code_dic[chr] = 7
        continue
    elif chr == 'Z':
        code_dic[chr] = 9
        continue

    # 3개 씩 끊어서 처리
    if count <= 2:
        count += 1
    else:
        value += 1
        count = 1
    code_dic[chr] = value

for i in s:
    s_number += str(code_dic[i])

print(convert_to_number(s_number))
