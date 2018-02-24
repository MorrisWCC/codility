def solution(A):
    # write your code in Python 3.6
    pass
    len_A = len(A)
    aux = [0] * (len_A+2)
    for i in range (0 , len_A):
        if len_A >= A[i] > 0:
            aux[A[i]] = 1
    for i in range (1 , len_A+1):
        if aux[i] == 0:
            return i;
    else:
        return len_A+1