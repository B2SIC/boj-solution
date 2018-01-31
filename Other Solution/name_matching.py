def name_mating(name_list):
    for i in range(len(name_list) - 1):
        for j in range(i + 1, len(name_list)):
            print(name_list[i], "-", name_list[j])


name_mating(["Tom", "Jerry", "Mike", "JayZ"])
