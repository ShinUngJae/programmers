def solution(my_string):
    return sum([int(i) for i in my_string if i.isdigit()])


# 다른 사람의 풀이
# 풀이 1
import re

def solution(my_string):
    return sum(int(n) for n in re.sub('[^1-9]', '', my_string))





# 풀이 2
def solution(my_string):
    answer = 0
    for i in my_string:
        try:
            answer = answer + int(i)
        except:
            pass

    return answer