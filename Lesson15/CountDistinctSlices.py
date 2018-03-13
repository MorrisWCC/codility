def solution(M, A):
    # write your code in Python 3.6
    pass
    
    len_A = len(A)
    aux_list = [False] * (M+1)
    slice_num = 0
    iter_left = 0
    iter_right = 0
    
    while iter_left < len_A and iter_right < len_A :
        if aux_list[A[iter_right]] == False : 
            slice_num += (iter_right - iter_left + 1 )
            aux_list[A[iter_right]] = True
            iter_right += 1        
        else :
            aux_list[A[iter_left]] = False
            iter_left += 1
    else:
        if slice_num > 1000000000:
            return 1000000000
        else :
            return slice_num