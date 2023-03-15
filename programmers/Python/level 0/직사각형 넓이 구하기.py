def solution(dots):
    width = []
    height = []
    for i in dots :
        width.append(i[0])
        height.append(i[1])

    return (max(width) - min(width)) * (max(height) - min(height))


# 다른 사람의 풀이
def solution(dots):
    return (max(dots)[0] - min(dots)[0])*(max(dots)[1] - min(dots)[1])