def result_score(score_list):
    sum = 0
    include_number = []

    for i in range(0, 5):
        include_number.append(score_list.index(sorted(score_list, reverse=True)[i]) + 1)
        sum += sorted(score_list, reverse=True)[i]

    print(sum)

    for score in sorted(include_number):
        print(score, end=' ')

input_list = []

for _ in range(8):
    input_list.append(int(input()))

result_score(input_list)
