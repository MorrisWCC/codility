def gcd(a, b):
    if (a % b == 0):
        return b
    else:
        return gcd(b, a % b)
 
def solution(N, M):
    gcd_of_two = gcd( N, M )
    lcm_of_two = N * M / gcd_of_two
    
    return int(lcm_of_two/M)