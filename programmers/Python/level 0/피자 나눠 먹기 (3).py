def solution(slice, n):
    return n // slice + 1 if n % slice != 0 else n // slice


# 다른 사람의 코드
def solution(slice, n):
    return ((n - 1) // slice) + 1