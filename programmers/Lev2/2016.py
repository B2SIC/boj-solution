def getDayName(a,b):
    # 2016 1 1 Friday

    month_list = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_list = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    sum_day = b - 1

    for i in range(1, a):
        sum_day += month_list[i]

    return day_list[sum_day % 7]

print(getDayName(5, 24))
