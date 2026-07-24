def solution(my_string, overwrite_string, s):
    answer = ''
    str1 = my_string[:s]
    return str1 + overwrite_string + my_string[s + len(overwrite_string):]
