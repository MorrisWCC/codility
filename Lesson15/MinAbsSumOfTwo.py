def solution(A):
    # write your code in Python 3.6
    pass
    
    A.sort()
    len_A = len(A)
    iter_left = 0
    iter_right = len_A - 1 
    
    rtn = abs(2 * A[-1])
    
    #DO Binary Search
    
    while iter_left < iter_right:
        tmp_min = abs(A[iter_left] + A[iter_right])
        
        if tmp_min < rtn :  
            rtn = tmp_min

        if abs(A[iter_left+1] + A[iter_right]) <= tmp_min:    
            iter_left += 1
            
        elif abs(A[iter_left] + A[iter_right-1]) <= tmp_min:  
            iter_right -= 1
            
        else:                         
            iter_left += 1 
            iter_right -= 1
    
    if rtn > abs(2 * A[0]) :
        return abs(2 * A[0])
    else:
        return rtn