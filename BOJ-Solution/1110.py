n = input()
init_n = int(n)
cycle = 0

while True:
    if int(n) < 10:
        n = n[-1] * 2
    else:
        n = n[1] + (str(int(n[0]) + int(n[1])))[-1]
    # print(n)
    cycle += 1

    if init_n == int(n):
        break
        
print(cycle)
