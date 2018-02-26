def solution(A, X):
    # write your code in Python 3.6
    pass
    fence_count = {}
    
    for size in A :
        fence_count[size] = fence_count.get(size,0)+1
    
    can_use_fence = []
    pens_number = 0
    
    for fence in fence_count:
        if fence_count[fence] < 2:
            continue
        elif fence_count[fence] < 4:
            can_use_fence.append(fence)
        else:
            if (fence ** 2) >= X :
                pens_number +=1
            can_use_fence.append(fence)
    can_use_fence.sort()
    len_cuf = len(can_use_fence)
    
    for i in range (0 , len_cuf):
        start = i+1
        end = len_cuf-1
        while start <= end :
            mid = (start+end)//2
            if can_use_fence[mid] * can_use_fence[i] >= X:
                end = mid-1
            else:
                start = mid+1
        pens_number += len_cuf - end - 1
        
    if pens_number > 1000000000:
        return -1
        
    return pens_number