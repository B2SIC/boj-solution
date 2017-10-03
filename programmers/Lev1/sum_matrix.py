def sumMatrix(A,B):
    for i in range(len(A)):
        for k in range(len(A[i])):
            A[i][k] = A[i][k] + B[i][k]
    return A

print(sumMatrix([[1,2], [2,3]], [[3,4], [5,6]]))
print(sumMatrix([[1,2], [2,3], [3,6]], [[3,4], [5,6], [7,8]]))