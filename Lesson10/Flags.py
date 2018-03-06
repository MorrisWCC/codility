def solution(A):
    # write your code in Python 3.6
    pass
    len_A = len(A)
    peaks = []
    
    if len_A < 3 :
        return 0
        
    for idx in range (1,len_A-1) :
        if A[idx-1] < A[idx] and A[idx] > A[idx+1] :
            peaks.append(idx)
    
    rtn = 0
    
    for idx in range ( 1, len(peaks)+1 ):
        if  idx*(idx-1) > len_A :
            break
        
        flags = idx
        last_position = -1-idx
        
        for pos in peaks :
            if idx > pos - last_position :
                continue
            
            last_position = pos
            flags -= 1
            
            if flags == 0:
                rtn = idx
                break
    
    return rtn