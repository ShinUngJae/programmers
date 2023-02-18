def solution(n) :
    n = n // 2 * 2
    return (n + 2) * (n / 4)

# 다른 사람의 풀이
def solution(n):
    return sum([i for i in range(2, n + 1, 2)])