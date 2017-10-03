def Jaden_Case(s):
    res = []
    for i in s.split():
        res.append(i.capitalize())
    return ' '.join(res)

def Jaden_Case_met2(s):
    return s.title()

print(Jaden_Case("3people unFollowed me for the last week"))
print(Jaden_Case_met2("3people unFollowed me for the last week"))
