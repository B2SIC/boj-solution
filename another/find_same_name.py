def find_same_name(name_list):
    result = set()
    for i in range(len(name_list) - 1):
        for j in range(i + 1, len(name_list)):
            if name_list[i] == name_list[j]:
                result.add(name_list[i])
    return result


print(find_same_name(["Tom", "Jerry", "Mike", "Tom"]))
print(find_same_name(["Tom", "Jerry", "Mike", "Tom", "Mike"]))