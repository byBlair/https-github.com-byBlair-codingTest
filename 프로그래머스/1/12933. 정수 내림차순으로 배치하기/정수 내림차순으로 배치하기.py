def solution(n):
    answer = 0
    answer = sorted(str(n), reverse=True)
    digit = int(''.join(answer))
    return digit