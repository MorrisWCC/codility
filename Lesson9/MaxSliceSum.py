def solution(A):
    # write your code in Python 3.6
    pass
    max_slice = A[0]
    max_slice_part = A[0]
    
    for idx in range ( 1, len(A) ) :
        max_slice_part = max(A[idx],max_slice_part+A[idx])
        max_slice = max (max_slice_part,max_slice)
    else:
        return max_slice
    