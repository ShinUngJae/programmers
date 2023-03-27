def solution(s):
    return str(min([int(i) for i in s.split()])) + " " + str(max([int(i) for i in s.split()]))


# 다른 사람의 풀이
def solution(s):
    s = list(map(int,s.split()))
    return str(min(s)) + " " + str(max(s))