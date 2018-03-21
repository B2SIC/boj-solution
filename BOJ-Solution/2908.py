n, m = input().split()
new_n = ""
new_m = ""

for i in range(2, -1, -1):
    new_n += n[i]
    new_m += m[i]

print(max(int(new_n), int(new_m)))