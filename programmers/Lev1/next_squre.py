import math

def nextSqure(n):
    squre_result = math.sqrt(n)
    if int(squre_result) == squre_result:
        return int((squre_result + 1) ** 2)
    else:
        return "no"

def nextSqure_2(n):
    if math.sqrt(n) % 1:
        return "no"
    else:
        return int((math.sqrt(n)+1)**2)

print(nextSqure(16))
print(nextSqure_2(16))
