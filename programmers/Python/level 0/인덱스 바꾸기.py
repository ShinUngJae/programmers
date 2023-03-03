def solution(my_string, num1, num2):
    temp1 = my_string[num1]
    temp2 = my_string[num2]
    temp_list = [i for i in my_string]
    temp_list[num1] = temp2
    temp_list[num2] = temp1
    return ''.join(temp_list)


# 다른 사람의 풀이
def solution(my_string, num1, num2):
    s = list(my_string)
    s[num1],s[num2] = s[num2],s[num1]
    return ''.join(s)