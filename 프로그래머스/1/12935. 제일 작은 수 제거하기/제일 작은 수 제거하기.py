def solution(arr):
    if len(arr) == 1:
        return [-1]
    remove_arr = arr.remove(min(arr))
    return arr