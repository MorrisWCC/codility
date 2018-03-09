# Task score 91 not 100。However time complexity detected is NlogN, some cases are not covered

def fibonacciDynamic(n):
    fib = [0] * (n + 2)
    fib[1] = 1
    for i in range(2, n + 2):
        fib[i] = fib[i - 1] + fib[i - 2]
        if fib[i] > n:
            return fib[i-1: 1: -1]
        elif fib[i] == n:
            return fib[i: 1: -1]


def solution(A):
    # write your code in Python 3.6
    pass
    len_A = len(A)
    position = [-1]
    moves    = [0]
    fib = fibonacciDynamic(len_A+1)
    next_pos = 0
    jumped_record = [False] * len_A
    
    while True :
        if next_pos == len(position) :
            return -1
        now_pos = position[next_pos]
        now_move = moves[next_pos]
        next_pos += 1
        
        for jump_len in fib :
            if now_pos + jump_len == len_A:
                return now_move + 1
            elif now_pos + jump_len > len_A \
                 or A[now_pos + jump_len] == 0 \
                 or jumped_record[now_pos + jump_len] == True :
                continue
            jumped_record[now_pos+jump_len] == True
            position.append(now_pos+jump_len);
            moves.append(now_move+1);