def solution(A, K):
    # write your code in Python 3.6
    pass
    if len(A) == 0:
        return A
    for i in range(0,K):
        tmp = A[len(A)-1]
        for j in range (len(A)-2,-1,-1):
            A[j+1] = A[j]
        A[0] = tmp
    return A