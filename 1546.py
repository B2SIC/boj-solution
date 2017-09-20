count = int(input())
score_list = list(map(int, input().split()))
result_list = []
mean = 0

M = max(score_list)

for i in range(0, count):
    result_list.append(score_list[i] / M * 100)

for j in range(0, count):
    mean += result_list[j]

mean /= count

print("%0.2f" % (mean))