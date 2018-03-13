def solution(A):
    # write your code in Python 3.6
    pass
    aux_dict = {}
    
    for num in A :
        abs_num = abs(num)
        aux_dict[abs_num] = aux_dict.get(abs_num,0)+1
    
    return len(aux_dict) 