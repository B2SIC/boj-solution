from math import sqrt

def abs_sign(n):
    if n >= 0:
        return n
    else:
        return -n


def abs_squre(n):
    n_squre = n * n
    return sqrt(n_squre)  # math.sqrt returns float.

print(abs_sign(187))
print(abs_sign(-187))
print(abs_squre(56))
print(abs_squre(-56))