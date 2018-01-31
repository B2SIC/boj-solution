def find_max(num_list):
    max_value = num_list[0]
    for i in range(1, len(num_list)):
        if num_list[i] > max_value:
            max_value = num_list[i]
    return max_value


def find_max_idx(num_list):
    # ============Recursive Version============
    # return num_list.index(find_max(num_list))
    # =========================================
    max_idx = 0
    for i in range(1, len(num_list)):
        if num_list[i] > num_list[max_idx]:
            max_idx = i
    return max_idx


print(find_max([5, 8, 11, 4, 9, 56, 2, 71, 3]))
print(find_max_idx([5, 8, 11, 4, 9, 56, 2, 71, 3]))