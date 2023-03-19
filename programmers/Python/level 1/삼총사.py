from itertools import combinations

def solution(number):
    answer = 0
    temp = 0
    combi_list = combinations(range(len(number)), 3)
    for i in combi_list :
        for j in i :
            temp += number[j]
        if temp == 0 :
            answer += 1
        temp = 0
    return answer


# 다른 사람의 풀이
def solution (number) :
    from itertools import combinations
    cnt = 0
    for i in combinations(number,3) :
        if sum(i) == 0 :
            cnt += 1
    return cnt