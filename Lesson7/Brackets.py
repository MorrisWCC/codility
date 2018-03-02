def solution(S):
    # write your code in Python 3.6
    pass
    my_list = []
    
    for char in S:
        len_list = len(my_list)
        if char == ')':
            if len_list != 0 and my_list[len_list-1] == '(':
                my_list.pop()
            else:
                my_list.append(char)
        elif char == '}':
            if len_list != 0 and my_list[len_list-1] == '{':
                my_list.pop()
            else:
                my_list.append(char)
        elif char == ']':
            if len_list != 0 and my_list[len_list-1] == '[':
                my_list.pop()
            else:
                my_list.append(char)
        else :
            my_list.append(char)
    else:
        if len(my_list) == 0:
            return 1
        else:
            return 0