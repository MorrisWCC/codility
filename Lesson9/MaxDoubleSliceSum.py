 def solution(A):
    # write your code in Python 3.6
    pass
    len_A = len(A)
    aux_first = [0] * len_A
    aux_second = [0] * len_A
    
    max_num = 0
    
    for idx in range ( 1, len_A-1 ) :
        aux_first[idx] = max(aux_first[idx-1]+A[idx],0)
    for idx in range ( len_A-2, 0, -1) :
        aux_second[idx] = max(aux_second[idx+1]+A[idx],0)
        
    for idx in range( 1, len_A-1 ):
        max_num = max(max_num,aux_first[idx-1]+aux_second[idx+1])
    
    
    return max_num