def solution(my_string):
    return sorted([int(i) for i in my_string if i.isdigit()])


# 다른 사람의 풀이
# 풀이 1
import re

def solution(my_string):
    return sorted(map(int, (list(re.sub('[^0-9]', '', my_string)))))

# 풀이 2
def solution(my_string):
    return sorted(map(int, filter(lambda s: s.isdigit(), my_string)))

# 풀이 3
import re

def solution(my_string):
    p = re.compile('[0-9]')
    A = list(map(int,p.findall(my_string)))
    A.sort()
    return A