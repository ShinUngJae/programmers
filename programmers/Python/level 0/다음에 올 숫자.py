def solution(common):
    if common[0] == common[1] :
        return common[0]
    elif 2 * common[1] == common[0] + common[2] :
        return common[-1] + (common[1] - common[0])
    else :
        return common[-1] * (common[1] // common[0])
    

# 다른 사람의 풀이
def solution(common):
    answer = 0
    a,b,c = common[:3]
    if (b-a) == (c-b):
        return common[-1]+(b-a)
    else:
        return common[-1] * (b//a)
    return answer