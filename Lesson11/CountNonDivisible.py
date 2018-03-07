#idea from https://codesays.com/2014/solution-to-count-non-divisible-by-codility/

import math
def solution(A):
    max_A = max(A)
    len_A = len(A)

    # count the frequency
    freq = {}
    for num in A:
        freq[num] = freq.get(num,0)+1

    # count each number divisor , trivial has 1
    divisors = {}
    for num in A:
        divisors[num] = [1]

    for div in range( 2, int(math.sqrt(max_A))+1 ):
        mul = div
        while mul  <= max_A:
            if mul in divisors and not div in divisors[mul]:
                divisors[mul].append(div)
            mul += div

    # del duplicate num
    
    for num in divisors:
        tmp = [ num/div for div in divisors[num] ]
        tmp = [ item for item in tmp if item not in divisors[num]]
        divisors[num].extend(tmp)
        
    rtn = []
    
    for num in A:
        tmp_sum = 0
        for div in divisors[num] :
            tmp_sum += freq.get(div,0)
        div_number = len_A -tmp_sum
        rtn.append(div_number)
 
    return rtn