def reverse(get_num):
    str_num = str(get_num)
    return reversed(str_num)

get_number = int(input("Input your number: "))

for i in reverse(get_number):
    print(i, end='')
