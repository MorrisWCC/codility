def solution(K, A):
    # write your code in Python 3.6
    pass
    len_A = len(A)
    rope_len = 0
    rtn = 0
    for num in A:
        rope_len += num
        if rope_len >= K :
           rtn += 1
           rope_len = 0
    else :
        return rtn
        