def solution(n) :
    temp = [0, 0, 1]
    m = n
    while (m - 1) > 0 : 
        if n == 0 :
            return temp[1]
        elif n == 1 :
            return temp[2]
        else :
            m -= 1
            temp = temp[1 :]
            temp.append((temp[0] + temp[1]) % 1234567)
    return temp[2]


# 다른 사람의 풀이
def solution(n):
    f_list = [0,1]
    for i in range(2,n+1):
        f_list.append((f_list[i-2]%1234567+f_list[i-1]%1234567)%1234567)
    return f_list[-1]