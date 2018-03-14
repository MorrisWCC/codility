def solution(A, B):
    # write your code in Python 3.6
    pass
    seg_num = len(A)
    
    if seg_num <= 1 :
        return seg_num
    
    overlapping_point = B[0]
    rtn = 1;
    for idx in range ( 1, seg_num ) :
        if A[idx] > overlapping_point :
            overlapping_point = B[idx]
            rtn += 1
    else :
        return rtn
        