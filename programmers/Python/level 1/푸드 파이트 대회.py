def solution(food):
    answer = ''
    for i in range(1, len(food)) :
        answer += str(i) * (food[i] // 2)
    answer += "0" + "".join([answer[i] for i in range(len(answer) - 1, -1, -1)])
    return answer


# 다른 사람의 풀이
def solution(food):
    answer ="0"
    for i in range(len(food)-1, 0,-1):
        c = int(food[i]/2)
        while c>0:
            answer = str(i) + answer + str(i)
            c -= 1
    return answer