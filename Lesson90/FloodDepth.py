def solution(A):
    left_height = 0
    bottom = 100000001
    rtn = 0
    for height in A:
        if height > left_height:
            depth = (left_height - bottom) if (left_height - bottom) > 0 else 0
            rtn = max(rtn, depth)
            left_height = height
            bottom = 100000001
            continue
        bottom = min(bottom, height)
        depth = height - bottom
        rtn = max(rtn, depth)
    return rtn