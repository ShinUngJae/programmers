from collections import deque

def solution(elements):

    elements_rotate = deque(elements)
    answer = set()
    for i in range(len(elements)) :
        if i == 0 :
            answer = set(elements)
            temp = elements
        else :
            elements_rotate.rotate(-1)
            temp = [i + j for i, j in zip(temp, elements_rotate)]
            answer = answer | set(temp)

    return len(answer)


# 다른 사람의 풀이
# 풀이 1
def solution(elements):
    answer = 0
    partial = list()
    temp_el = elements*2

    for i in range(1,len(elements)+1):
        for j in range(len(elements)):
            partial.append(sum(temp_el[j:j+i]))

    answer = len(set(partial))

    return answer

# 풀이 2
def solution(elements):
    ll = len(elements)
    res = set()

    for i in range(ll):
        ssum = elements[i]
        res.add(ssum)
        for j in range(i+1, i+ll):
            ssum += elements[j%ll]
            res.add(ssum)
    return len(res)

# 풀이 3
def solution(elements):
    N = len(elements)
    elements *= 2
    return len(set(sum(elements[j:j+n]) for j in range(N) for n in range(1, N+1)))