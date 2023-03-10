def solution(n) :
    a_list = [False] * (n + 1)

    for i in range(2, (int(n ** 0.5) + 1)) :
        if a_list[i] == False :
            for j in range(i + i, n + 1, i) :
                a_list[j] = True
    return sum(a_list)


# 다른 사람의 코드
def get_divisors(n):
    return list(filter(lambda v: n % v ==0, range(1, n+1)))

def solution(n):
    return len(list(filter(lambda v: len(get_divisors(v)) >= 3, range(1, n+1))))