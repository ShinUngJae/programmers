def solution(strArr):
    return [strArr[i].upper() if i % 2 == 1 else strArr[i].lower() for i in range(len(strArr))]


# 다른 사람의 풀이
def solution(strArr):
    return [s.lower() if i % 2 == 0 else s.upper() for i, s in enumerate(strArr)]