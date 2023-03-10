def solution(my_string):
    answer = ""
    for i in my_string :
        if i not in answer :
            answer += i
    return answer


# 다른 사람의 코드
def solution(my_string):
    return ''.join(dict.fromkeys(my_string))