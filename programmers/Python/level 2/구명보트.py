from collections import deque

def solution(people, limit):

    answer = 0
    people = deque(sorted(people))
    while len(people) > 1 :
        left = people.popleft()
        right = people.pop()
        if left + right <= limit :
            answer += 1
        else :
            people.appendleft(left)
            answer += 1

    if len(people) == 1 :
        answer += 1

    return answer


# 다른 사람의 풀이
### 전체 사람 수에서 "굳이 둘이서 같이 탄 빈도 수"를 빼면 보트 수가 나옴
def solution(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer