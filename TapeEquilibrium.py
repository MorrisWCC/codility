def solution(A):
    # write your code in Python 3.6
    pass
    gap = 9223372036854775807
    tmp = 0
    cumulative =[]
    len_A = len(A)
    if len_A == 0 :
        return 0
        
    for i in range(len_A):
        tmp += A[i]
        cumulative.append(tmp)
    for i in range (1,len_A):
        tmp = abs(cumulative[len_A-1]-2*cumulative[i-1])
        if gap > tmp:
            gap = tmp
    return gap