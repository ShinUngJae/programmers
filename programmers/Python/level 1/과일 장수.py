def solution(k, m, score):
    answer = 0
    score = sorted(score, reverse = True)
    for i in range(len(score) // m) :
        answer += min([score[j] for j in range(i * m, (i + 1) * m)]) * m
    return answer


# 다른 사람의 풀이
def solution(k, m, score):
    return sum(sorted(score)[len(score)%m::m])*m