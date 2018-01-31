string = input()

while True:
    if len(string) < 10:
        print(string)
        break
    else:
        string_10 = string[0:10]
        string = string[10:]
        print(string_10)