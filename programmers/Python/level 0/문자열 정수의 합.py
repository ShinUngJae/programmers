def solution(num_str):
    return sum([int(i) for i in num_str])


# 다른 사람의 풀이
def solution(num_str):
    return sum(map(int, list(num_str)))