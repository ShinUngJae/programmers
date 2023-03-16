def solution(n):
    temp = 1
    n2 = 0
    while n > n2 :
        if (temp % 3 == 0) or ("3" in str(temp)) :
            temp += 1
        else :
            temp += 1
            n2 += 1
    return temp - 1


# 다른 사람의 풀이
def solution(n):
    answer = 0
    for _ in range(n):
        answer += 1
        while answer % 3 == 0 or '3' in str(answer):
            answer += 1
    return answer