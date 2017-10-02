def sort_dictionary(dic):
    return sorted(dic.items(), key=lambda x:x[0])

print(sort_dictionary({"김철수":78, "이하나":97, "정진원":88}))