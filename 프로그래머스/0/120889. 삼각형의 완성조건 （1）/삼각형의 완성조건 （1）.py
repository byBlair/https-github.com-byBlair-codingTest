def solution(sides):
    answer = 0
    sides_sorted = sorted(sides)
    if sides_sorted[2] < sides_sorted[0] + sides_sorted[1]:
        return 1
    else :
        return 2
