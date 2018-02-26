def solution(N, S, T):
    # write your code in Python 3.6
    pass
    rtn = -1
    block_size = N/2
    
    raft_left_front = block_size ** 2
    raft_left_back = block_size ** 2
    raft_right_front = block_size ** 2
    raft_right_back = block_size ** 2
    
    for barrels  in S.split():
        row = int(barrels[:-1])-1
        col = ord(barrels[-1]) - ord('A')
        if (row < block_size):
            if (col < block_size):
                raft_left_front -= 1
            else:
                raft_right_front -= 1
        else:
            if (col < block_size) :
                raft_left_back -= 1
            else:
                raft_right_back -= 1
    
    accommodation_L_F = min ( raft_left_front , raft_right_back)
    accommodation_R_B = min ( raft_left_front , raft_right_back)
    accommodation_R_F = min ( raft_right_front , raft_left_back)
    accommodation_L_B = min ( raft_right_front , raft_left_back)
    
    for dwarfs in T.split():
        row = int(dwarfs[:-1])-1
        col = ord(dwarfs[-1]) - ord('A')
        
        if (row < block_size) : 
            if (col < block_size):
                accommodation_L_F -= 1
            else:
                accommodation_R_F -= 1
        else:
            if (col < block_size):
                accommodation_L_B -= 1
            else:
                accommodation_R_B -= 1
        
        if (accommodation_L_F < 0 or accommodation_L_B < 0 or accommodation_R_F < 0 or accommodation_R_B < 0):
                return -1
    return int (accommodation_L_F+accommodation_L_B+accommodation_R_F+accommodation_R_B)
    