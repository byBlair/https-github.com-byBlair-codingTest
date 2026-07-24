def solution(n):
    answer = []
    
    for ch in str(n)[::-1]:
        answer.append(int(ch))   
    return answer