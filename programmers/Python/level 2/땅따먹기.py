# 다른 사람의 풀이
# DP(Dynamic Programming) : 동적계획법 사용

def solution(land):
    
    for i in range(len(land)) :
        if i == 0 :
            continue
        else :
            for j in range(4) :
                land[i][j] += max([land[i - 1][k] for k in range(4) if j != k])
    
    return max(land[i])