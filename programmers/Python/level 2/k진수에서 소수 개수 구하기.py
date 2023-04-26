# 내 풀이
def decimal(n) :

    if n == 1 :
        return False
    
    for i in range(2, int((n ** 0.5) + 1)) :
        if n % i == 0 :
            return False
        
    return True

def solution(n, k):
    answer = 0
    number = ""

    while n :
        if n % k != 0 :
            number = str(n % k) + number
            n = n // k
        else :
            if (number != "") and (decimal(int(number))) :
                answer += 1
            number = ""
            n = n // k

    if (number != "") and (decimal(int(number))) :
        answer += 1 
    return answer