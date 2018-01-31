N, X = map(int, input().split())
num_list = list(map(int, input().split()))
result = []

for i in range(0, N):
    if num_list[i] < X:
        result.append(str(num_list[i]))

print(" ".join(result))