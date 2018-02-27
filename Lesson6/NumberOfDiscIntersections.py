def solution(A):
    # write your code in Python 3.6
    pass
    pairs = 0
    postive_aux = []
    negtive_aux = []
    
    for idx,num in enumerate(A) :
        postive_aux.append(idx+num)
        negtive_aux.append(idx-num)

    postive_aux.sort()
    negtive_aux.sort()
    
    disc_count = 0
    for idx,num in enumerate(postive_aux):
        while disc_count < len(A) and num >= negtive_aux[disc_count] :
            pairs += disc_count - idx
            disc_count += 1
            
    if pairs >  10000000 : 
        return -1
    else:
        return pairs