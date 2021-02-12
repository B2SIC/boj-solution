apple = int(input())
moreApple = int(input())

if apple % 2 == 0:
    klaudia = apple // 2 + (moreApple // 2)
    natalia = apple // 2 - (moreApple // 2)
else:
    klaudia = (apple // 2) + 1 + (moreApple // 2)
    natalia = (apple // 2) - (moreApple // 2)

print(klaudia)
print(natalia)