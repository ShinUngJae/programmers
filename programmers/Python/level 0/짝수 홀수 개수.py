def solution(num_list):
    result = [0, 0]
    result[0] = sum([i % 2 == 0 for i in num_list])
    result[1] = len(num_list) - result[0]
    return result

# 다른 사람의 풀이
def solution(num_list):
    answer = [0,0]
    for n in num_list:
        answer[n%2]+=1
    return answer