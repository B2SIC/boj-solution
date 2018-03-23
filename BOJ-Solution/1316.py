def del_overlap(target):
    re_list = [target[0]]

    # [c c c a b b] => [c a b]
    for i in range(len(target) - 1):
        if target[i] != target[i + 1]:
            re_list.append(target[i + 1])
    return re_list

n = int(input())
count = 0

for i in range(n):
    deny = False
    chr_list = [chr(x) for x in range(ord('a'), ord('z') + 1)]

    word = input()
    alpha_list = del_overlap(list(word))

    for j in alpha_list:
        try:
            del chr_list[chr_list.index(j)]
        except ValueError:
            deny = True
            break

    if deny == True:
        continue
    else:
        count += 1

print(count)
