def solution(array, n):
    temp1 = {i : abs(i - n) for i in array}
    temp2 = [i for i, j in temp1.items() if j == min(list(temp1.values()))]
    return min(temp2)


# 다른 사람의 코드
solution=lambda a,n:sorted(a,key=lambda x:(abs(x-n),x))[0]