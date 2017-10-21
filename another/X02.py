# list를 생성하여 한 학급당 40명인 3학급의 성적을 발생시켜 저장 (난수 발생 메커니즘 및 2차원 list 이용)
# 각 학급별 최고점수와 최저점수 및 평균 출력
# 전체 학급의 최고 점수와 최저점수 및 전체 평균 점수 출력

import random

all_sum = 0
scores_list = [[], [], []]
max_min_score = [[], []]

for i in range(len(scores_list)):
    for k in range(0, 40):
        scores_list[i].append(random.randint(0, 100))

for j in range(len(scores_list)):
    all_sum += sum(scores_list[j])
    max_min_score[0].append(max(scores_list[j]))
    max_min_score[1].append(min(scores_list[j]))
    print("***********************************")
    print("%d반 평균은 %f" % (j + 1, sum(scores_list[j]) / 40))
    print("최고 점수는 %d" % max(scores_list[j]))
    print("최저 점수는 %d" % min(scores_list[j]))
    print("***********************************")

print("***********************************")
print("전체 평균은 %f" % (all_sum / 120))
print("전체 최고 점은 %d" % max(max_min_score[0]))
print("전체 최저 점은 %d" % min(max_min_score[1]))
print("***********************************")
print(scores_list)