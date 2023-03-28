def solution(s):
    temp = ""
    answer = ""
    for i in range(len(s)) :
        if s[i].isalpha() or s[i].isdigit() :
            temp += s[i]
        else :
            if (temp != "") and (temp[0].isdigit()) :
                answer += temp.lower()
                answer += " "
                temp = ""
            elif (temp != "") and (temp[0].isalpha()) :
                answer += temp.capitalize()
                answer += " "
                temp = ""
            else :
                answer += " "
    if (temp != "") and (temp[0].isdigit()) :
        answer += temp.lower()
    elif (temp != "") and (temp[0].isalpha()) :
        answer += temp.capitalize()
                
    return answer


# 다른 사람의 풀이
def solution(s):
    answer = ''
    for i in s.lower().split(' '):
        if answer == '':
            answer += i.capitalize()
        else:
            answer += ' '+i.capitalize()
    return answer