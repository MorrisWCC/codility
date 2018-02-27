def solution(K, C, D):
    # write your code in Python 3.6
    pass
    clean={}
    dirty={}
    max_pairs = 0
    
    for num in C:
        clean[num] = clean.get(num,0)+1
    for num in D:
        dirty[num] = dirty.get(num,0)+1
    
    for num in clean :
        while clean[num] >= 2 :
            max_pairs += 1
            clean[num] -= 2
    
    for num in dirty :
        if clean.get(num) == 1 and dirty[num] >= 1 and K >= 1:
            dirty[num] -= 1
            clean[num] -= 1
            K -= 1
            max_pairs += 1
   
    for num in dirty :
        while dirty[num] >= 2 and K >= 2:
            dirty[num] -= 2
            K -= 2
            max_pairs += 1
    
    return max_pairs