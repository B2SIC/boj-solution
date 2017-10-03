def gcdlcm(a,b):
    default_a = a
    default_b = b

    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b

    return [a, (default_a * default_b) // a]

print(gcdlcm(32, 12))
print(gcdlcm(128,224))