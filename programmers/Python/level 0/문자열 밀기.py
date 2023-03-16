def solution(A, B):
    for i in range(len(A)) :
        if A == B :
            return i
        else :
            temp = A[-1] + A[: -1]
            A = temp
    return -1


# 다른 사람의 풀이
# 풀이 1
solution=lambda a,b:(b*2).find(a)