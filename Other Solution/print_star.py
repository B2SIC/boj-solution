num = input("Input your number: ")
star = "\u2605"
starnum = 3

for i in range(len(num)):
    ch = int(num[i])
    for j in range(starnum * ch):
        print(star, end='')
    print()