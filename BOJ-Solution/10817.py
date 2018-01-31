A, B, C = map(int, input().split())

if A > B and B > C: # A > B > C
    print(B)
elif A > C and C > B: # A > C > B
    print(C)
elif B > A and A > C: # B > A > C
    print(A)
elif B > C and C > A: # B > C > A
    print(C)
elif C > A and A > B: # C > A > B
    print(A)
elif C > B and B > A: # C > B > A
    print(B)
# ------------------
if A == B and B != C:
    print(A)
elif A == C and C != B:
    print(A)
elif B == C and A != B:
    print(B)

# 세 숫자 모두 크기가 똑같을 때
if A == B and B == C:
    print(A)