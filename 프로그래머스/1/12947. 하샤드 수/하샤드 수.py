def solution(x):
    hashad = 0
    for i in str(x):
        hashad += int(i)
        
    if x % hashad == 0:
        return True
    else : 
        return False