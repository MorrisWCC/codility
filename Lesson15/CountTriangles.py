def solution(A):
    len_A = len(A)
    triangular_num = 0
    A.sort()
 
    for idx_P in range( 0, len_A-2) :
        idx_R = idx_P + 2
        for idx_Q in range( idx_P+1, len_A-1 ) :
            while idx_R < len_A and (A[idx_P] + A[idx_Q] > A[idx_R]) :
                idx_R += 1
            triangular_num += idx_R - idx_Q - 1  
    
    return triangular_num