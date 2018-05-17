num = input("Input your number: ")
star = "\u2605"
starnum = 3
i = 0

while True:
    if i >= len(num):
        break
    ch = int(num[i])
    for j in range(starnum * ch):
        print(star, end='')
    print()
    i += 1
