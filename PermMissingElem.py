def solution(A):
    # write your code in Python 3.6
    pass
    list_sum = sum(A)
    total_sum = ((len(A)+1) * (len(A)+2))/2  # sum equal N*N+1/2
    
    return int ( total_sum - list_sum )