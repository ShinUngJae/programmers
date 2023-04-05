def solution(n):
    answer = 0
    for i in range(1, n + 1) :
        j = n
        for j in range(1, n - i + 2) :
            if (2 * i + j - 1) * j / 2 == n :
                answer += 1
                break
            elif (2 * i + j - 1) * j / 2 > n :
                break
                
    return answer