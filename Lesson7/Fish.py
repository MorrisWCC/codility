def solution(A, B):
    rtn = 0
    stack_downstream = []

    for fish_number in range(0,len(A)):
        if B[fish_number] == 1:
            stack_downstream.append(A[fish_number])
        else:
            while len(stack_downstream) != 0:
                if stack_downstream[len(stack_downstream) -1 ] < A[fish_number]:
                    stack_downstream.pop()
                else:
                    break
            else:
                rtn += 1
    rtn += len(stack_downstream)
 
    return rtn