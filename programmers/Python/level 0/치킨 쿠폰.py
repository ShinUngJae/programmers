def solution(chicken):
    answer = 0
    while chicken >= 10 :
        answer += chicken // 10
        chicken = chicken // 10 + chicken % 10
    return answer


# 다른 사람의 코드
# 풀이 1
def solution(chicken):
    return int(chicken*0.11111111111)

# 풀이 2
def solution(chicken):
    answer = (max(chicken,1)-1)//9
    return answer

# 풀이 3
def solution(chicken):
    answer = 0
    while chicken >= 10:
        chicken, mod = divmod(chicken, 10)
        answer += chicken
        chicken += mod
    return answer