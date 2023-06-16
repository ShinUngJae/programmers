def solution(my_string, index_list):
    return "".join([my_string[i] for i in index_list])


# 다른 사람의 풀이
def solution(my_string, index_list):
    return ''.join(map(lambda x: my_string[x], index_list))