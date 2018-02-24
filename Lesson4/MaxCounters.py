def solution(N, A):
    # write your code in Python 3.6
    pass
    rtn = [0] * N
    max_num = 0
    update_num = 0
    len_A = len(A)
    for i in range(0,len_A):
        if A[i] == N+1 :
            update_num = max_num
        else:
            if (rtn[A[i]-1] < update_num):
                rtn[A[i]-1] = update_num
            rtn[A[i]-1] += 1
            if (rtn[A[i]-1] > max_num):
                max_num = rtn[A[i]-1]
    for i in range (0 , N):
        if (rtn[i] < update_num ):
            rtn[i] = update_num
    return rtn