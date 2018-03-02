from extratypes import Tree  # library with types used in the task

def calculate_height(T,height):
    if T == None :
        return 0
    if T.l == None and T.r == None:
        return 0
    else:
        return max(calculate_height(T.l,height),calculate_height(T.r,height))+1

def solution(T):
    # write your code in Python 3.6
    pass
    height = 0
    height = calculate_height(T,height)
    
    return height


