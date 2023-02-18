def solution(dot):
    return ((dot[0] > 0) & (dot[1] > 0)) * 1 + ((dot[0] < 0) & (dot[1] > 0)) * 2 + ((dot[0] < 0) & (dot[1] < 0)) * 3 + ((dot[0] > 0) & (dot[1] < 0)) * 4

# 다른 사람의 풀이
def solution(dot):
    quad = [(3,2),(4,1)]
    return quad[dot[0] > 0][dot[1] > 0]