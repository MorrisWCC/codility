# mod 2**B[i] 時不可用暴力法 不然會變成 O(L ** 2)
# 參考 https://codesays.com/2014/solution-to-ladder-by-codility/ 將mod的時間複雜度往下降
# 或者 此篇 https://stackoverflow.com/questions/6670715/mod-of-power-2-on-bitwise-operators/6670766

def solution(A, B):
    # write your code in Python 3.6
    pass
    len_A = len(A)
    B = [(1 << item) - 1 for item in B]
    fib = [0] * (len_A + 2)
    fib[1] = 1
    rtn = []
    for i in range(2, len_A + 2):
        fib[i] = fib[i - 1] + fib[i - 2]
    for idx in range ( 0, len_A ):
        rtn.append(fib[A[idx]+1] & B[idx])
    return rtn