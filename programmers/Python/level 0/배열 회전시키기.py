# 내 코드
from collections import deque

def solution(numbers, direction):
    a = deque(numbers)
    if direction == 'right' :
        a.rotate(1)
    else :
        a.rotate(-1)
    return list(a)


# 다른 사람의 코드
def solution(numbers, direction):
    return [numbers[-1]] + numbers[:-1] if direction == 'right' else numbers[1:] + [numbers[0]]