def distin(get_text):
    text_list = []
    get_text = get_text.lower()

    for i in get_text:
        if i.isalpha() == True:
            text_list.append(i)

    result1 = "".join(text_list)
    result2 = "".join(reversed(result1))

    if result1 == result2:
        answer = True
    else:
        answer = False

    return answer

type = input()
print(distin(type))