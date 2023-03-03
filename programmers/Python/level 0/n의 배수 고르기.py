def solution(n, numlist):
    return [i for i in numlist if i % n == 0]


# 다른 사람의 풀이
def solution(n, numlist):
    return list(filter(lambda v: v%n==0, numlist))