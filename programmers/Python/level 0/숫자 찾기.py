def solution(num, k):
    return str(num).index(str(k)) + 1 if str(k) in str(num) else -1


# 다른 사람의 코드
# 풀이 1
def solution(num, k):
    try:
        return str(num).index(str(k)) + 1
    except ValueError:
        return -1