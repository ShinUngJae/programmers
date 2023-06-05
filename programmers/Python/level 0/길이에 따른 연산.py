from functools import reduce

def solution(num_list):
    return sum(num_list) if len(num_list) > 10 else reduce(lambda x, y : x * y, num_list, 1)


# 다른 사람의 풀이
# 풀이 1
def solution(num_list):
    if len(num_list) >= 11:
        return eval('+'.join(list(map(str, num_list))))
    else:
        return eval('*'.join(list(map(str, num_list))))
# 풀이 2
from math import prod
def solution(num_list):
    return sum(num_list) if len(num_list)>=11 else prod(num_list)