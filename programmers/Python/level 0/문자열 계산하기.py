def solution(my_string):
    num_list = [i for i in my_string.split(' ') if i.isdigit()]
    cal_list = [i for i in my_string.split(' ') if i not in num_list]
    answer = 0
    
    for i in range(len(num_list)) :
        if i == 0 :
            answer = int(num_list[i])
        elif cal_list[i - 1] == "+" :
            answer += int(num_list[i])
        else :
            answer -= int(num_list[i])
    return answer


# 다른 사람의 코드
# 풀이 1
def solution(my_string):
    return sum(int(i) for i in my_string.replace(' - ', ' + -').split(' + '))

# 풀이 2
def solution(my_string):
    return eval(my_string)