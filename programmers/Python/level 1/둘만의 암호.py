def solution(s, skip, index):
    answer = ''
    skip_list = [ord(i) for i in skip]
    index_count = 0

    for j in s :
        jj = ord(j)
        while index > index_count :
            
            jj += 1
            
            if jj > 122 :
                jj -= 26
            
            if jj not in skip_list :
                index_count += 1
                
        index_count = 0
        answer += chr(jj)
        
    return answer


# 다른 사람의 풀이
# 풀이 1
from string import ascii_lowercase

def solution(s, skip, index):
    result = ''

    a_to_z = set(ascii_lowercase)
    a_to_z -= set(skip)
    a_to_z = sorted(a_to_z)
    l = len(a_to_z)

    dic_alpha = {alpha:idx for idx, alpha in enumerate(a_to_z)}

    for i in s:
        result += a_to_z[(dic_alpha[i] + index) % l]

    return result

# 풀이 2
def solution(s, skip, index):
    alphas = [chr(a) for a in range(ord("a"), ord("z")+1) if chr(a) not in skip]
    return "".join([alphas[(alphas.index(a) + index) % len(alphas)] for a in s])