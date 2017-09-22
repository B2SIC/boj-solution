def solution(n,m):
    answer = 1
    for i in range(m):
        if n == 0:
            break
        else:
            answer *= n
            n -= 1
    return answer
