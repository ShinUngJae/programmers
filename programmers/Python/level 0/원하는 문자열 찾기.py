def solution(myString, pat):
    return 1 if pat.lower() in myString.lower() else 0


# 다른 사람의 풀이
def solution(myString, pat):
    return int(pat.lower() in myString.lower())