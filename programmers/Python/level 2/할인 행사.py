from collections import Counter

def solution(want, number, discount) :
    answer = 0
    want_counter = Counter({i : j  for i, j in zip(want, number)})
    for i in range(len(discount) - sum(number) + 1) :
        discount_counter = Counter(discount[i : i + sum(number)])
        if want_counter == discount_counter :
            answer += 1
    return answer