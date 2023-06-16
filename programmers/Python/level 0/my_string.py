import re

def solution(rny_string):
    return re.sub("m", "rn", rny_string)


# 다른 사람의 풀이
def solution(rny_string):
    return rny_string.replace('m', 'rn')