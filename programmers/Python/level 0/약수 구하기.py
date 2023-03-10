def solution(n):
    answer = []
    for i in range(1, int((n ** 0.5) + 1)) :
        if n % i == 0 :
            answer.append(i)
            answer.append(n // i)
    return sorted(list(set(answer)))


# 다른 사람의 코드
# 풀이 1
def solution(n):
    return list(filter(lambda v: n % v == 0, [i for i in range(1, n//2+1)])) + [n]

# 풀이 2
def solution(n):
    return [v for v in range(1,n+1) if (n/v).is_integer()]