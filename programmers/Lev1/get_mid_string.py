def string_middle(str):
    if len(str) % 2 == 0:
        return str[(len(str) // 2) - 1] + str[len(str) // 2]
    else:
        return str[len(str) // 2]

print(string_middle("power"))
print(string_middle("test"))