s = input().lower()
count_list = [0] * 26

for word in s:
    count_list[ord(word) - 97] += 1

for pr in count_list:
    print(pr, end=' ')