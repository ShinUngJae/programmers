def solution(s) :
    answer = 0
    x_num = 0
    y_num = 0
    x = ""
    for i in range(len(s)) :
        if x == "" :
            x = s[i]
            x_num += 1
        else :
            if s[i] == x :
                x_num += 1
            else :
                y_num += 1
        if (x_num == y_num) or (i == len(s) - 1) :
            answer += 1
            x = ""
            x_num, y_num = 0, 0
        print(i, x, answer)

    return answer


# 다른 사람의 풀이
def solution(s):
    answer = 0
    sav1=0
    sav2=0
    for i in s:
        if sav1==sav2:
            answer+=1
            a=i
        if i==a:
            sav1+=1
        else:
            sav2+=1
    return answer