def solution(str_list, ex):
    return ''.join([i for i in str_list if ex not in i])


# 다른 사람의 풀이
def solution(str_list, ex):
    return ''.join(filter(lambda x: ex not in x, str_list))