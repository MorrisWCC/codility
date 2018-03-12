def test( blocks, largest_num, input_list, mid) :
    if mid < largest_num :
        return False
    
    _sum = 0
    _cnt = 1
    
    for num in input_list :
        _sum += num
        if _sum > mid :
            _cnt += 1
            _sum = num
    else: 
        if _cnt <= blocks :
            return True
        else :
            return False

def solution(K, M, A):
    # write your code in Python 3.6
    pass
    max_A = max(A)
    len_A = len(A)
    
    start = 0
    end   = ( len_A * max_A )
    rtn = 0
    
    while start <= end :
        mid = (start+end)//2
        
        if (test( K, max_A, A, mid)):
            end = mid - 1
            rtn = mid
        else :
            start = mid + 1
    
    return int(rtn)