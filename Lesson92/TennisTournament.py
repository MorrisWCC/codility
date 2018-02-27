def solution(P, C):
    # write your code in Python 3.6
    pass
    
    if P == 1 :
        return 0
    
    count = P//2
    
    if C >= count :
        return count
    else:
        return C