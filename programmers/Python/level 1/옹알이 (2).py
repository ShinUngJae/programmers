import re

def solution(babbling):
    answer = 0
    babbling_list = ["aya", "ye", "woo", "ma"]
    babbling_twice = [i * 2 for i in babbling_list]
    for i in babbling :
        for j in range(len(babbling_list)) :
            if babbling_twice[j] in i :
                i = "a"
        for j in range(len(babbling_list)) :              
            if babbling_list[j] in i :
                i = re.sub(babbling_list[j], " ", i)
                
        i = re.sub(" ", "", i)     
        if i == "" :
            answer += 1
            
    return answer


# 다른 사람의 풀이
# 풀이 1
def solution(babbling):
    answer = 0
    for i in babbling:
        for j in ['aya','ye','woo','ma']:
            if j*2 not in i:
                i=i.replace(j,' ')
        if len(i.strip())==0:
            answer +=1
    return answer

# 풀이 2
def solution(babbling):
    count = 0

    for b in babbling:
        if "ayaaya" in b or "yeye" in b or "woowoo" in b or "mama" in b:
            continue    
        if not b.replace("aya", " ").replace("ye", " ").replace("woo", " ").replace("ma", " ").replace(" ", ""):
            count += 1

    return count