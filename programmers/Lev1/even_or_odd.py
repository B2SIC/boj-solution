def evenOrOdd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

'''
Think about this

def evenOrOdd(num):
    return (num % 2 and "Odd") or "Even"
'''

print(evenOrOdd(111))
print(evenOrOdd(12))