import math

def solution(N):
    # write your code in Python 3.6
    pass
    cnt = 0
    
    for value in range (1 , math.floor(math.sqrt(N))+1):
        mod = N % value
        div = N / value
        if mod == 0:
            if div != value:
                cnt +=2
            else:
                cnt +=1
    return cnt