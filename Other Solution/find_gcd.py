def gcd(a, b):
    i = min(a, b)
    while True:
        if a % i == 0 and b % i == 0:
            return i
        i = i -1


def gcd_euclid(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def gcd_euclid_recursive(a, b):
    if b == 0:
        return a
    return gcd_euclid_recursive(b, a % b)


print(gcd(12, 26))
print(gcd(60, 24))
print(gcd(81, 27))
print()
print(gcd_euclid(12, 26))
print(gcd_euclid(60, 24))
print(gcd_euclid(81, 27))
print()
print(gcd_euclid_recursive(12, 26))
print(gcd_euclid_recursive(60, 24))
print(gcd_euclid_recursive(81, 27))