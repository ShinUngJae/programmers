def solution(spell, dic):
    for i in dic :
        temp = 0
        for j in spell :
            if j in i :
                temp += 1
        if temp == len(spell) :
            return 1        
    return 2


# 다른 사람의 풀이
# 풀이 1
def solution(spell, dic):
    spell = set(spell)
    for s in dic:
        if not spell-set(s):
            return 1
    return 2

# 풀이 2
def solution(spell, dic):
    spell = set(spell)
    return int(any(d for d in dic if not spell - set(d))) or 2