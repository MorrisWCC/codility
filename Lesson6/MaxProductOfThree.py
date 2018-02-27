def solution(A):
    # write your code in Python 3.6
    pass
    A.sort()
    len_A = len(A)
    
    if (A[len_A-1] * A[len_A-2] * A[len_A-3])  > (A[0] * A[1] * A[len_A-1]):
        return A[len_A-1] * A[len_A-2] * A[len_A-3]
    else:
        return A[0] * A[1] * A[len_A-1]