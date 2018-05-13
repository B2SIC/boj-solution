def get_element(data_list, a, b):
    length = len(data_list)

    if a > 0 and b > 0:
        if a > b:
            return data_list[b-1:a]
        else:
            return data_list[a-1:b]
    else:
        if a > b:
            return data_list[b + length : a + length + 1]
        else:
            return data_list[a + length : b + length + 1]

# Test Case:
if __name__ == "__main__":
    get_list = [1,2,3,4,5,6,7,8,9,10]
    print(get_element(get_list, -1, -5))
    print(get_element(get_list, -5, -1))
    print(get_element(get_list, 1, 4))
    print(get_element(get_list, 4, 1))
    print(get_element(get_list, 1, 10))
    print(get_element(get_list, 10, 1))