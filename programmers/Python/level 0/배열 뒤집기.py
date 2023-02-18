def solution(num_list):
    return [num_list[i] for i in range(len(num_list) - 1, -1, -1)]

# 다른 사람의 풀이 1
def solution(num_list):
    return num_list[::-1]

# 다른 사람의 풀이 2
def solution(num_list):
    num_list.reverse()
    return num_list