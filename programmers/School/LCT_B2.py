def solution(instr, keystr):
    key_list = []
    for i in instr.split(","):
        for j in i.rsplit("="):
            key_list.append(j)

    for k in range(len(key_list)):
        if key_list[k] == keystr:
            return int(key_list[k + 1])

    return -1

print(solution("Lang=10,Math=20,Eng=30", "Math"))
