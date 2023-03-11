def solution(n):
    answer = 1
    temp = 1
    while n >= temp :
        answer += 1
        temp *= answer
    return answer - 1


# 다른 사람의 풀이
from math import factorial

def solution(n):
    k = 10
    while n < factorial(k):
        k -= 1
    return k