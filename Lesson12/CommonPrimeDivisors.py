def gcd(a, b):
    if (a % b == 0):
        return b
    else:
        return gcd(b, a % b)
        
def solution(A, B):
    
    cnt = 0
    for idx in range( 0, len(A) ):
        a = A[idx]
        b = B[idx]
        gcd_of_two = gcd(a, b)
        while True:
            divisor = gcd(a, gcd_of_two)
            if divisor == 1:
                break
            a /= divisor
        while True:
            divisor = gcd(b, gcd_of_two)
            if divisor == 1:
                break
            b /= divisor
        if a == 1 and b == 1 :
            cnt += 1
            
    return cnt