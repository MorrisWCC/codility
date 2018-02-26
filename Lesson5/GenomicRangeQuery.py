 # you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, P, Q):
    # write your code in Python 3.6
    pass
    len_S = len(S)
    len_M = len(P)
    nucleotide_A = [0] * (len_S+1)
    nucleotide_C = [0] * (len_S+1)
    nucleotide_G = [0] * (len_S+1)
    nucleotide_T = [0] * (len_S+1)
    rtn = []
    i = 0
    for dna in S:
        nucleotide_A[i+1] = nucleotide_A[i]
        nucleotide_C[i+1] = nucleotide_C[i]
        nucleotide_G[i+1] = nucleotide_G[i]
        nucleotide_T[i+1] = nucleotide_T[i]
        if dna == 'A' :
            nucleotide_A[i+1] += 1
        elif dna == 'C' :
            nucleotide_C[i+1] += 1
        elif dna == 'G' :
            nucleotide_G[i+1] += 1
        else:
            nucleotide_T[i+1] += 1
        i += 1    

    for idx in range (0 , len_M):
        A_count =  nucleotide_A[Q[idx]+1]- nucleotide_A[P[idx]]
        C_count =  nucleotide_C[Q[idx]+1]- nucleotide_C[P[idx]]
        G_count =  nucleotide_G[Q[idx]+1]- nucleotide_G[P[idx]]
        T_count =  nucleotide_T[Q[idx]+1]- nucleotide_T[P[idx]]
        
        if A_count > 0 :
            rtn.append(1)
        elif C_count > 0 :
            rtn.append(2)
        elif G_count > 0 :
            rtn.append(3)
        else :
            rtn.append(4)
    
    return rtn
        
        