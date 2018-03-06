def solution(A):
    # write your code in Python 3.6
    pass
    len_A = len(A)
    peaks = []
    
    for idx in range ( 1, len_A-1) :
        if A[idx-1] < A[idx] and A[idx] > A[idx+1] :
            peaks.append(idx)
            
    rtn = 0
    
    for size in range( len(peaks), 0, -1 ) :
        if len_A % size == 0:
            block_size = len_A // size
            block = [0] * size
            block_cnt = 0
            for pos in peaks:
                block_idx = pos // block_size
                if block[block_idx] == 0 :
                    block[block_idx] = 1
                    block_cnt += 1
 
            if block_cnt == size:
                return size
 
    return rtn