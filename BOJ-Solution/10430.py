integer_list = list(map(int, input().split()))
temp = list(integer_list)
r1 = (temp[0]+temp[1])%temp[2]
r2 = (temp[0]%temp[2]+temp[1]%temp[2])%temp[2]
r3 = (temp[0]*temp[1])%temp[2]
r4 = (temp[0]%temp[2]*temp[1]%temp[2])%temp[2]
print(r1)
print(r2)
print(r3)
print(r4)