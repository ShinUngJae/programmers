def solution(n):
    answer = 0
    while n > 1 :
        if n % 2 == 0 :
            n = n // 2
        else :
            n = n // 2
            answer += 1
    return answer + 1


# 다른 사람의 풀이
def solution(n):
    return bin(n).count('1')