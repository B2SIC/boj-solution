n = int(input())
num = input()
num_list = []
total = 0

for i in num:
    num_list.append(int(i))

for k in range(0,n):
    total += num_list[k]

print(total)