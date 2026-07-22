def solution(a, b):
    a = str(a)
    b = str(b)
    ab = int(a + b)
    ba = int(b + a)
    return max(ab, ba)