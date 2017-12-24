A = int(input())
B = int(input())
C = int(input())

result = A * B * C
str_result = str(result)
num_list = [0] * 10

for num in str_result:
    num_list[int(num)] += 1

for i in num_list:
    print(i)
