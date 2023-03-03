def solution(my_string):
    return ''.join([i for i in my_string if i not in 'aeiou'])


# 다른 사람의 풀이
import re
def solution(my_string):
    return re.sub('[aeiou]', '', my_string)