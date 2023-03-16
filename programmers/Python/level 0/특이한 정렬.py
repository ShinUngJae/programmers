def solution(numlist, n):
    temp_list = sorted([[abs(i - n), -i]  for i in numlist])
    return [-i[1] for i in temp_list]


# 다른 사람의 풀이
def solution(numlist, n):
    answer = sorted(numlist,key = lambda x : (abs(x-n), n-x))
    return answer