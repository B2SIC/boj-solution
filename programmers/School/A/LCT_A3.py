def solution(num_list, n):
    if n <= 0 or n > len(num_list):
        return -1

    sorted_list = sorted(num_list, reverse=True)
    # 1번째 => index 0
    # 2번째 => index 1
    # n번째 => index n-1
    return sorted_list[n - 1]

# 8 7 4(*) 3 2 1 => return 4
print(solution([1, 4, 3, 7, 8, 2], 3))
