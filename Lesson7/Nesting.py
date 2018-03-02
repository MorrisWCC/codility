 def solution(S):
    # write your code in Python 3.6
    pass
    cnt = 0

    for char in S:
        if char == '(':
            cnt += 1
        else:
            cnt -= 1
            if cnt < 0 :
                return 0
    else:
        if cnt == 0 :
            return 1
        else:
            return 0