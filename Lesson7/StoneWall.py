 def solution(H):
    # write your code in Python 3.6
    pass
    len_H = len(H)
    stones = 0
    stack = []
    stack_idx = 0
    for i in range(len_H):
        while stack_idx > 0 and stack[stack_idx - 1] > H[i]:
            stack_idx -= 1
            stack.pop()
        if stack_idx > 0 and stack[stack_idx - 1] == H[i]:
            pass
        else:
            stones += 1
            stack.append(H[i])
            stack_idx += 1
    return stones