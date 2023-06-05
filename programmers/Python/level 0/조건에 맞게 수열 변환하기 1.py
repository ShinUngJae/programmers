def solution(arr):
    for i in range(len(arr)) :
        if (arr[i] >= 50) and (arr[i] % 2 == 0) :
            arr[i] /= 2
        elif (arr[i] < 50) and (arr[i] % 2 == 1) :
            arr[i] *= 2
    return arr


# 다른 사람의 풀이
def solution(arr):
    return [num/2 if num>=50 and num%2==0 else (num*2 if num<50 and num%2==1 else num) for num in arr]