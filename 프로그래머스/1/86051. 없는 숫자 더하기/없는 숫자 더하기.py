def solution(numbers):
    answer = 0
    alpha = [1,2,3,4,5,6,7,8,9,0]
    for i in alpha:
        if i not in numbers:
            answer += i
    return answer