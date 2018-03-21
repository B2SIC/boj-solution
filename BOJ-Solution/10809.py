import string

s = input()

for i in string.ascii_lowercase:
    print(s.find(i), end=' ')