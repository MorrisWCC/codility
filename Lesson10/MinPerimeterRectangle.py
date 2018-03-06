import math
def solution(N):
    # write your code in Python 3.6
    pass
    min_perimeter = 10000000000
    for value in range ( 1, math.floor(math.sqrt(N))+1) :
        div = N // value
        mod = N % value
        if mod == 0:
            min_perimeter = min(min_perimeter,2*(div+value))
    else:
        return min_perimeter