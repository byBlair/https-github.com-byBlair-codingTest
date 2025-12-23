def solution(my_string):
    aeiou = 'aeiou'
    answer = ''
    for i in my_string:
        if i not in aeiou :
            answer += i
    return answer
        