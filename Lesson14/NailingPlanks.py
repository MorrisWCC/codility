#idea from 
#https://github.com/mbobesic/algorithms-playground/blob/master/codility/NailingPlanks.py
# brilliant solution
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def test( A, B, C, mid ):
    nails = [0] * ( 2 * ( len(C) + 1) )

    for idx in range ( 0, mid ) :
        nails[C[idx]] += 1
        
    for idx in range ( 1, len(nails) ) :
        nails[idx] += nails[idx-1]
        
    for idx in range ( 0, len(A) ) :
         if ( nails[B[idx]] - nails[A[idx]-1] ) == 0 :
            return False
            
    else :
        return True
        
def solution(A, B, C):
    # write your code in Python 3.6
    pass
    len_of_range = len(C)
    start = 0
    end = len_of_range
    rtn = -1
    while start <= end :
        mid = ( start + end ) // 2
        if test ( A, B, C, mid ) :
            end = mid - 1
            rtn = mid
        else :
            start = mid + 1
    else :
        return rtn