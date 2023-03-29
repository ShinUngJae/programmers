def solution(A, B):
    
    answer = 0
    AA = sorted(A)
    BB = sorted(B, reverse = True)
    for i in range(len(AA)) :
        answer += AA[i] * BB[i]
    return answer


# 다른 사람의 풀이
def solution(A, B):
    return sum([a * b for a, b in zip(sorted(A), sorted(B, reverse=True))])