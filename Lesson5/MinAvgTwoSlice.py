# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    pass
    min_value = (A[0]+A[1])/2.0
    index = 0
    len_A = len(A)
    for i in range(1,len_A-2):
        if (A[i]+A[i+1])/2.0 < min_value:
            min_value = (A[i]+A[i+1])/2.0
            index = i
        elif (A[i]+A[i+1]+A[i+2])/3.0 < min_value:
            min_value = (A[i]+A[i+1]+A[i+2])/3.0
            index = i
    if (A[len_A-1] + A[len_A-2]) / 2.0 < min_value:
        index = len_A-2
        
    return index