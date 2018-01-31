'''
Q. 30 이상의 정수를 입력 받아서 0부터 입력 받은 숫자까지의 난수를 발생 시켜
입력받은 숫자가 1000번 발생할 때까지 반복하여 각 숫자 별로 생성된 횟수와 전체 시도한 횟수를 출력하는 프로그램 작성
'''

import random

count = 0
final_count = 0
number_dic = {}
result_list = []

get_num = int(input("30 이상의 원하는 정수를 입력하세요: "))

if get_num >= 30:
    while count != 1000:
        random_number = random.randint(0, get_num)
        final_count += 1

        if random_number == get_num:
            count += 1
        number_dic[random_number] = number_dic.get(random_number, 0) + 1

    result_list = sorted(number_dic.items(), key=lambda x:x[0])

    for i in range(0, len(result_list)):
        print("%d 이(가) 발생한 횟수는 %d번 입니다." % (result_list[i][0], result_list[i][1]))

    print("0부터 입력한 숫자 %d이(가) 1000번 발생할 때까지의 총 반복 횟수는 %d번 입니다." % (get_num, final_count))
else:
    print("You can input number >= 30")

