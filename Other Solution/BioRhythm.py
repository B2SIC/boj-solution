import datetime, math

# 태어난 날짜 ~ 현재 날짜까지의 Day 계산
def calc_date():
    try:
        print("===========BioRhythm 측정기=============")
        get_year = int(input("태어난 해를 입력해주세요: "))
        get_month = int(input("태어난 월을 입력해주세요: "))
        get_day = int(input("태어난 일을 입력해주세요: "))

        birth = datetime.date(get_year, get_month, get_day)
        now = datetime.date.today()
        return (datetime.date(now.year, now.month, now.day) - birth).days
    except:
        print("Error Log: 잘못된 값을 입력했습니다.")
        print("Error Log: 바이오리듬 측정기를 다시 불러옵니다..")
        return calc_date()

life_long = calc_date()
print()

###################
### 바이오리듬 계산 ###
# 공식: sin((lifeDate / value) * 2 * 3.141592654) * 100
###################

print("==============계산 결과=================")
bio_float = 3.141592654
value_dic = {'신체지수': 23, '감성지수': 28, '지성지수': 33, '지각지수': 38}

for value in sorted(value_dic):
    calc = int(math.sin((life_long / value_dic[value]) * 2 * bio_float) * 100)
    print("%s: %d" % (value, calc))

    if calc >= 0:
        print("■" * (calc // 10))
    else:
        print(" " * (10 - (-calc // 10)) + "■" * (-calc // 10))

print("======================================")
