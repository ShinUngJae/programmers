def solution(angle):
    if 0 < angle < 90 :
        return 1
    elif angle == 90 :
        return 2
    elif 90 < angle < 180 :
        return 3
    else :
        return 4



# 다른 사람의 풀이
def solution(angle):
    answer = (angle // 90) * 2 + (angle % 90 > 0) * 1
    return answer