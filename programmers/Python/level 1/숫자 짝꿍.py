from collections import Counter

def solution(X, Y):
    X_Counter = Counter(X)
    Y_Counter = Counter(Y)
    temp = X_Counter & Y_Counter
    temp_sort = sorted(temp, reverse = True)
    answer = ""
    
    if temp == {} :
        answer = "-1"
    elif temp_sort == ['0'] :
        answer = "0"
    else :
        for i in temp_sort :
            answer += i * temp[i]
    
    return answer


# 다른 사람의 풀이
def solution(X, Y):
    answer = ''

    for i in range(9,-1,-1) :
        answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))

    if answer == '' :
        return '-1'
    elif len(answer) == answer.count('0'):
        return '0'
    else :
        return answer
