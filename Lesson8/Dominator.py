def solution(A):
    # write your code in Python 3.6
    pass
    candidate = 0 
    candidate_cnt = 0
    candidate_idx = -1
    
    len_A = len(A)
    
    for idx in range ( 0, len_A ):
        if candidate_cnt == 0 :
            candidate_cnt = 1
            candidate     = A[idx]
            candidate_idx = idx
        else:
            if candidate == A[idx] :
                candidate_cnt += 1
            else :
                candidate_cnt -= 1
    
    cnt = 0
    for value in A :
        if value == candidate :
            cnt += 1
    else :
        if cnt <= len_A // 2:
            return -1
        else:
            return candidate_idx