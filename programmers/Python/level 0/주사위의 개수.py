def solution(box, n):
    return (box[0] // n) * (box[1] // n) * (box[2] // n) 


# 다른 사람의 풀이
import math

def solution(box, n):
    return math.prod(map(lambda v: v//n, box))