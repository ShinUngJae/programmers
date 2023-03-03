def solution(n):
    if n**(1/2) == int(n**(1/2)) :
        a = 1
    else :
        a = 0
    
    answer = 0
    for i in range(1, int((n ** (1/2))) + 1) :
        print(i)
        if n % i == 0 :
            answer += 1

    answer = answer * 2 - a
    
    return answer


# 다른 사람 코드
def solution(n):
    return len(list(filter(lambda v: n % (v+1) == 0, range(n))))