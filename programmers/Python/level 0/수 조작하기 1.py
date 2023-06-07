def solution(n, control):
    return n + control.count("w") - control.count("s") + control.count('d') * 10 - control.count('a') * 10


# 다른 사람의 풀이
def solution(n, control):
    key = dict(zip(['w','s','d','a'], [1,-1,10,-10]))
    return n + sum([key[c] for c in control])