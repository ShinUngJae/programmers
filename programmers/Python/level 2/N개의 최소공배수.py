from functools import reduce

def solution(arr):
    
    n = 2
    answer = 1
    while n <= max(arr) :
        if len([i for i in arr if i % n == 0]) > 1 :
            answer *= n
            arr = [i // n if i % n == 0 else i for i in arr]
        else :
            n += 1
            
    return reduce(lambda x, y : x * y, arr, answer)