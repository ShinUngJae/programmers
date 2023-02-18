def solution(my_string) :
    return ''.join([my_string[i] for i in range(len(my_string) - 1, -1, -1)])


# 다른 사람의 풀이 1
def solution(my_string):
    return my_string[::-1]

# 다른 사람의 풀이 2
def solution(my_string):
    return ''.join(list(reversed(my_string)))