def solution(X, A):
    # write your code in Python 3.6
    pass
    aux = [-1] * X
    rtn = 0
    for i in range(0 , len(A)):
        if aux[A[i]-1] == -1 :
            aux[A[i]-1] = i
    for i in range(0 , X):
        if aux[i] == -1:
            return -1
        if aux[i] > rtn:
            rtn = aux[i]
    else:
        return rtn