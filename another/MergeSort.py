def solution(A, B):
    a_count = 0
    b_count = 0
    answer = []
    while a_count < len(A) and b_count < len(B):
        if A[a_count] < B[b_count]:  # B의 원소가 A보다 클 경우
            answer.append(A[a_count])
            a_count += 1
        elif A[a_count] > B[b_count]:  # A의 원소가 B의 원소보다 클 경우
            answer.append(B[b_count])
            b_count += 1
        elif A[a_count] == B[b_count]:  # A == B (Find)
            return a_count + b_count
    return -1
