def water_melon(n):
    water_string = "수박"
    if n % 2 == 0:
        return water_string * (n // 2)
    else:
        return water_string * (n // 2) + "수"

print(water_melon(3))
print(water_melon(10))