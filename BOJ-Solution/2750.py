n = int(input())
number_list = []

for i in range(n):
    number = int(input())
    number_list.append(number)

for j in sorted(number_list):
    print(j)