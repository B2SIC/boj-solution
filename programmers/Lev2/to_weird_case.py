def toWeirdCase(s):
    count = 0
    result = ""

    for i in s.split():
        for k in i:
            if count % 2 == 0:
                result += k.upper()
                count += 1
            else:
                result += k.lower()
                count += 1
        count = 0
        result += " "

    return result.rstrip()

print(toWeirdCase("try hello world"))
print(toWeirdCase("VTl eyNwtB Iw gWCzr"))