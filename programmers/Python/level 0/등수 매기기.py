def solution(score):
    score_list = [sum(i) / 2 for i in score]
    sort_list = sorted(list(set(score_list)), reverse = True)
    answer = [0 for i in range(len(score_list))]
    temp = 0
    
    for i in range(len(sort_list)) :
        temp += 1
        answer = [temp if score_list[j] == sort_list[i] else answer[j] for j in range(len(score_list))]
        temp += score_list.count(sort_list[i]) - 1
        
    return answer


# 다른 사람의 풀이
# 풀이 1
def solution(score):
    a = sorted([sum(i) for i in score], reverse = True)
    return [a.index(sum(i))+1 for i in score]

# 풀이 2
def solution(score):
    rank = sorted([sum(s) / 2 for s in score], reverse=True)
    rankDict = {}
    for i, r in enumerate(rank):
        if r not in rankDict.keys():
            rankDict[r] = i + 1
    return [rankDict[sum(s) / 2] for s in score]