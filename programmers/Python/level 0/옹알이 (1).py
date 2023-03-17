import re

def solution(babbling):
    babbling_list = ["aya", "ye", "woo", "ma"]
    answer = 0
    for i in babbling :
        for j in babbling_list :
            while j in i :
                if j in i :
                    i = re.sub(j, "0", i)
                    
        if i.isdigit() :
            answer += 1
                
    return answer


# 다른 사람의 풀이
import re

def solution(babbling):
    regex = re.compile('^(aya|ye|woo|ma)+$')
    cnt=0
    for e in babbling:
        if regex.match(e):
            cnt+=1
    return cnt