def solution(my_string, letter):
    return ''.join([my_string[i] for i in range(len(my_string)) if my_string[i] != letter])

# 다른 사람의 풀이
def solution(my_string, letter):
    return my_string.replace(letter, '')