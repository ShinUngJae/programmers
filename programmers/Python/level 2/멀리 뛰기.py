def combi(a, b) :
    answer = 1
    for i in range(a, a - b, -1) :
        answer *= i
        answer //= a - i + 1
    return answer

def solution(n):
    answer = 0
    one = n
    two = 0
    while one >= 0 :
        if one == n :
            answer += 1
            one -= 2
            two += 1
        else :
            count = one + two
            answer += combi(count, two) % 1234567
            one -= 2
            two += 1

    return answer % 1234567