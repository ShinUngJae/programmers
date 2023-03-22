def solution(cards1, cards2, goal):
    
    one = 0
    two = 0
    for i in goal :
        
        if (one < len(cards1)) & (cards1[one] == i) :
            one += 1
            one = min(one, len(cards1) - 1)
        elif (two < len(cards2)) & (cards2[two] == i) :
            two += 1
            two = min(two, len(cards2) - 1)
        else :
            return "No"

    return "Yes"


# 다른 사람의 풀이
def solution(cards1, cards2, goal):
    for g in goal:
        if len(cards1) > 0 and g == cards1[0]:
            cards1.pop(0)       
        elif len(cards2) >0 and g == cards2[0]:
            cards2.pop(0)
        else:
            return "No"
    return "Yes"