w = input().lower()

word_dic = {}

for i in w:
    word_dic[i] = word_dic.get(i, 0) + 1

word_dic = sorted(word_dic.items(), key=lambda x:x[1], reverse=True)

if len(word_dic) >= 2:
    if word_dic[0][1] == word_dic[1][1]:
        print("?")
    else:
        print(word_dic[0][0].upper())
else:
    print(word_dic[0][0].upper())