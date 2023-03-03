def solution(hp):
    return (hp // 5) + (hp % 5) // 3 + (hp % 5) % 3


# 다른 사람의 풀이
def solution(hp):
    answer = 0
    for ant in [5, 3, 1]:
        d, hp = divmod(hp, ant)
        answer += d
    return answer