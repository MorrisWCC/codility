# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, K):
    # write your code in Python 3.6
    pass
    if ( A%K == 0):
        return int(B/K) - int(A/K) + 1
    return int(B/K) - int((A-1)/K)