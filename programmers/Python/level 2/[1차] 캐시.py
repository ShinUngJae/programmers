from collections import deque

def solution(cacheSize, cities) :
    
    cache = deque()
    answer = 0
    for i in cities :
        i = i.lower()
        if cacheSize == 0 :
            return len(cities) * 5
        elif i in cache :
            cache.remove(i)
            cache.append(i)
            answer += 1
        else :
            if len(cache) < cacheSize :
                cache.append(i)
                answer += 5
            else :
                cache.popleft()
                cache.append(i)
                answer += 5

    return answer


# 다른 사람의 풀이
def solution(cacheSize, cities):
    import collections
    cache = collections.deque(maxlen=cacheSize)
    time = 0
    for i in cities:
        s = i.lower()
        if s in cache:
            cache.remove(s)
            cache.append(s)
            time += 1
        else:
            cache.append(s)
            time += 5
    return time