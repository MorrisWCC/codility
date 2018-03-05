def solution(A):
    # write your code in Python 3.6
    pass
    max_profit_base = 200000+1
    max_profit = 0
    max_profit_so_far = 0
    for value in A:
        max_profit_base = min(max_profit_base,value)
        max_profit_so_far = max(0,value- max_profit_base)
        max_profit = max(max_profit,max_profit_so_far)
    else :
        return max_profit