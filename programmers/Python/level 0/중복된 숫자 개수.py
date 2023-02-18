def solution(array, n):
    return sum([i == n for i in array])

# 다른 사람의 풀이
def solution(array, n):
    return array.count(n)