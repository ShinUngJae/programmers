def solution(balls, share):
    answer = 1
    for i in range(balls, balls - share, -1) :
        answer *= i
    
    for j in range(share) :
        answer /= (j + 1)
    return int(answer)


# 다른 사람의 코드
# 풀이 1
import math

def solution(balls, share):
    return math.comb(balls, share)

# 풀이 2
import math
def solution(balls, share):
    return math.factorial(balls)/(math.factorial(balls-share)*math.factorial(share))