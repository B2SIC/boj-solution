n = input()
n_list = n.split()

result = 0

for i in n_list:
    result += int(i)**2
result %= 10

print(result)