import math

def solution(N, P, Q):
    
    # get prime
    prime_table = [False]*2+[True]*(N-1)
    prime = []
    prime_count = 0
    for num in range(2, int(math.sqrt(N))+1):
        if prime_table[num] == True:
            prime.append(num)
            prime_count += 1
            multiple = num * num
            while multiple <= N:
                prime_table[multiple] = False
                multiple += num
    for num in range(int(math.sqrt(N))+1, N+1):
        if prime_table[num] == True:
            prime.append(num)
            prime_count += 1
 


    semi_prime = [0] * (N+1)
    for i in range(0,prime_count-1):
        for j in range(i, prime_count):
            if prime[i] * prime[j] > N:
                break
            semi_prime[prime[i]*prime[j]] = 1


    for idx in range( 1, N+1 ) :
        semi_prime[idx] += semi_prime[idx-1]

    rtn = [0] * len(P)
    for idx in range( 0, len(P) ) :
        rtn[idx] = semi_prime[Q[idx]] - semi_prime[P[idx]-1]
 
    return rtn