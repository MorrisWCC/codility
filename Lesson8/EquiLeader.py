def solution(A):
    len_A = len(A)
    candidate = 0
    candidate_cnt = 0
    candidate_idx = -1

    for idx in range( 0, len_A ):
        if candidate_cnt == 0:
            candidate = A[idx]
            candidate_idx = idx
            candidate_cnt += 1
        else:
            if A[idx] == candidate:
                candidate_cnt += 1
            else:
                candidate_cnt -= 1
    
    leader_cnt = 0
    for value in A :
        if value == candidate :
            leader_cnt += 1
    if leader_cnt <= len_A // 2:
        return 0
    else:
        leader = candidate
 
    rtn = 0
    leader_cnt_prefix = 0
    
    for idx in range(0,len_A):
        if A[idx] == leader:
            leader_cnt_prefix += 1
            
        if leader_cnt_prefix > (idx+1)//2 and leader_cnt-leader_cnt_prefix > (len_A-idx-1)//2:
            rtn += 1
 
    return rtn