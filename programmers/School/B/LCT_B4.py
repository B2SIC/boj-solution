def solution(plain, keyarr):
    idx = 0
    max_idx = len(keyarr) - 1
    for i in range(len(plain)):
        plain[i] += keyarr[idx]
        idx += 1
        if idx > max_idx:
            idx = 0
    return plain

print(solution([3, 4, 8, 5, 4, 4, 15], [2, 5, 1]))