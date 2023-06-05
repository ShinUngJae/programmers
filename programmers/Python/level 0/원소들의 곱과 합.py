from functools import reduce

def solution(num_list):
    return int(reduce(lambda x, y : x * y, num_list, 1) < sum(num_list) ** 2)


# 다른 사람의 풀이
def solution(num_list):
    s=sum(num_list)**2
    m=eval('*'.join([str(n) for n in num_list]))
    return 1 if s>m else 0