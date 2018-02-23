def solution(N):
    # write your code in Python 3.6
    pass
    rtn = 0
    gap = 0
    while (N > 0 and N %2 == 0):
        N = N>>1
    while (N > 0):
        if (N%2 == 0):
            gap+=1
        else:
            if gap!=0 :
                rtn = max(rtn,gap)
            gap = 0
        N = N>>1
    return rtn