def solution(my_string, is_prefix):
    return 1 if my_string[ : len(is_prefix)] == is_prefix else 0


# 다른 사람의 풀이
def solution(my_string, is_prefix):
    return int(my_string.startswith(is_prefix))