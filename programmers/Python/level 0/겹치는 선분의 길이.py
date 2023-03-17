from collections import Counter

def solution(lines):
    lines_list = []
    answer = 0
    
    for i in lines :
        for j in range(i[0], i[1]) :
            lines_list.append([j, j + 1])
            
    lines_unique = list(set([tuple(i) for i in lines_list]))
    for j in lines_unique :
        if lines_list.count(list(j)) > 1 :
            answer += 1
    
    return answer


# 다른 사람의 풀이
# 풀이 1
def solution(lines):
    sets = [set(range(min(l), max(l))) for l in lines]
    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])

# 풀이 2
def solution(lines):
    import collections
    return sum(1 for k, v in collections.Counter((i, i + 1) for x, y in lines for i in range(min(x, y), max(x, y))).items() if v > 1)