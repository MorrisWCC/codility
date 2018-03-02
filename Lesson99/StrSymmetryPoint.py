def solution(S):
    # write your code in Python 3.6
    pass
    len_S = len(S)
    if len_S % 2 == 0:
        return -1
    
    middle = len_S // 2
    start = 0
    end = len_S - 1
    while start < middle :
        if S[start] == S[end]:
            start += 1
            end -= 1
        else:
            return -1
            
    return middle