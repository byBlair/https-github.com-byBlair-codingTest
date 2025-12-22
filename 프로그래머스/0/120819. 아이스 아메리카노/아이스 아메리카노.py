def solution(money):
    answer = []
    cups = money // 5500
    save = money % 5500
    return [cups,save]