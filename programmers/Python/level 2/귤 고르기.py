from collections import Counter

def solution(k, tangerine):
    answer = 0
    temp1 = list(Counter(tangerine).values())
    tangerine_count = sorted(temp1)
    
    while k > 0 : 
        tan = tangerine_count.pop()
        if k >= tan :
            k -= tan
            answer += 1
        else :
            answer += 1
            break

    return answer


# 다른 사람의 풀이
from collections import Counter

def solution(k, tangerine):
    counter = Counter(tangerine)
    tangerine.sort(key = lambda t: (-counter[t], t))
    return len(set(tangerine[:k]))