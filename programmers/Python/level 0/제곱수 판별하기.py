def solution(n):
    return 1 if n ** (1/2) == int(n ** (1/2)) else 2


# 다른 사람의 풀이
# 풀이 1
def solution(n):
    return 1 if (n ** 0.5).is_integer() else 2

# 풀이 2
def solution(n):
    return 1 if (n ** 0.5) % 1 == 0 else 2

# 풀이 3
import math

def solution(n):
    return 1 if int(math.sqrt(n)) ** 2 == n else 2