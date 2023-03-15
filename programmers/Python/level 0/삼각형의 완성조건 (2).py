def solution(sides):
    return sum(sides) - max(sides) + min(sides) - 1


# 다른 사람의 풀이
def solution(sides):
    return 2 * min(sides) - 1