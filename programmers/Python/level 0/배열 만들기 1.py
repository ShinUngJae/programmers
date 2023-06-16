def solution(n, k):
    return [i for i in range(0, n + 1, k) if i != 0]


# 다른 사람의 풀이
def solution(n, k):
    return [i for i in range(k,n+1,k)]