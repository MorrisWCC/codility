def solution(S):
    # write your code in Python 3.6
    pass
    rtn = -1
    input_list = S.split(" ")
    for str in input_list:
        letter_count = 0
        digits_count = 0
        for char in str:
            if 48 <= ord(char) <= 57:
                digits_count += 1
            elif 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122 :
                letter_count += 1
        if digits_count % 2 == 1 and letter_count %2 == 0 :
            if digits_count + letter_count == len(str):
                if len(str) > rtn :
                    rtn = len(str)
    return rtn