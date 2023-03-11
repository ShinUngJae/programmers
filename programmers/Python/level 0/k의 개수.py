def solution(i, j, k):
    return sum([str(m).count(str(k)) for m in range(i, j + 1)])


# 다른 사람의 코드
def solution(i, j, k):
    return sum(map(lambda v: str(v).count(str(k)), range(i, j+1)))