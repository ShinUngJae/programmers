def solution(my_string):
    answer = []
    temp = '0'
    for i in my_string :
        if i.isdigit() :
            temp += i
        else :
            answer.append(int(temp))
            temp = '0'
    answer.append(int(temp))
    return sum(answer)


# 다른 사람의 코드
# 풀이 1
import re

def solution(my_string):
    return sum([int(i) for i in re.findall(r'[0-9]+', my_string)])

# 풀이 2
import re

def solution(my_string):
    return sum(map(int, re.findall(r"\d+", my_string)))

# 풀이 3
def solution(my_string):
    s = ''.join(i if i.isdigit() else ' ' for i in my_string)
    return sum(int(i) for i in s.split())