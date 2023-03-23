def solution(ingredient):

    answer = 0
    answer_list = []
    for i in range(len(ingredient)) :
        if i in [0, 1, 2] :
            answer_list.append(ingredient[i])
        elif (answer_list[-3 :] == [1, 2, 3]) and (ingredient[i] == 1) :
            answer += 1
            answer_list.pop()
            answer_list.pop()
            answer_list.pop()
        else :
            answer_list.append(ingredient[i])
    
    return answer


# 다른 사람의 풀이
def solution(ingredient):
    s = []
    cnt = 0
    for i in ingredient:
        s.append(i)
        if s[-4:] == [1, 2, 3, 1]:
            cnt += 1
            for i in range(4):
                s.pop()
    return cnt