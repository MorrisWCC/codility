def solution(A):
    # write your code in Python 3.6
    pass
    numbers={}
    rtn = 0
    for num in A:
        numbers[num] = numbers.get(num,0) + 1
    rtn = len(numbers)
    
    return rtn