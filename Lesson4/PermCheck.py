def solution(A):
    # write your code in Python 3.6
    pass
    len_A = len(A)
    aux = [0] * (len_A+1)
    for i in range (0 , len(A)):
        if A[i] > len_A:
            return 0
        aux[A[i]] = 1
    for i in range (1 , len(aux)):
        if aux[i] == 0:
            return 0
    else:
        return 1