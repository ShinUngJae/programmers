def solution(M, N):
    return min(M, N) - 1 + (max(M, N) - 1) * min(M, N)


# 다른 사람의 풀이
def solution(M, N):
    return (M * N) - 1