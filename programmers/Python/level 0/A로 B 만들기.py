from collections import Counter

def solution(before, after):
    return 1 if Counter(before) == Counter(after) else 0


# 다른 사람의 코드
def solution(before, after):
    return 1 if sorted(before)==sorted(after) else 0