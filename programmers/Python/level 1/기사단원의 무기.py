def divisor(num) :
    answer = 0
    for i in range(1, int(num ** 0.5) + 1) :
        if num % i == 0 :
            answer += 1
    if num ** 0.5 == int(num ** 0.5) :
        return answer * 2 - 1
    else :
        return answer * 2 


def solution(number, limit, power):
    answer = 0
    for i in range(1, number + 1) :
        if divisor(i) > limit :
            answer += power
        else :
            answer += divisor(i)
    return answer


# 다른 사람의 풀이
def cf(n): # 공약수 출력
    a = []
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            a.append(n//i)
            a.append(i)
    return len(set(a))
def solution(number, limit, power):
    return sum([cf(i) if cf(i)<=limit else power for i in range(1,number+1)])