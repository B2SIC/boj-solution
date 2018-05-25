from McCluskey import McCluskey

input_list = ["3 4 0 1 2 3",
              "3 6 0 1 2 5 6 7",
              "4 4 0 2 12 13",
              "4 8 0 1 2 3 4 5 6 7",
              "5 2 30 31",
              "6 2 62 63",
              "4 8 0 1 2 3 5 7 8 10",
              "4 9 0 1 2 3 5 7 8 15 10",
              "4 11 0 1 2 8 3 5 10 12 7 13 15",
              ]

for exp in input_list:
    tmp_input = list(map(int, exp.split()))

    number_of_var = tmp_input[0]
    minterm_list = []

    for i in range(2, 2 + tmp_input[1]):
        minterm_list.append(tmp_input[i])

    mc = McCluskey(number_of_var, minterm_list)
    mc.solution()

    print()
