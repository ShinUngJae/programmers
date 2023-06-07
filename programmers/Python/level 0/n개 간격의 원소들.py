def solution(num_list, n):
    return [num_list[i] for i in range(0, len(num_list), n)]


# 다른 사람의 풀이
def solution(num_list, n):
    return num_list[::n]