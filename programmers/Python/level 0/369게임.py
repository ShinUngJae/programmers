# 내 코드
def solution(order):
    return len([i for i in str(order) if i in ["3", "6", "9"]])

# 다른 사람의 코드
# 풀이 1
def solution(order):
    return sum(map(lambda x: str(order).count(str(x)), [3, 6, 9]))

# 풀이 2
def solution(order):
    answer = 0
    order = str(order)
    return order.count('3') + order.count('6') + order.count('9')

# 풀이 3
def solution(order):
    answer = len([1 for ch in str(order) if ch in "369"])
    return answer