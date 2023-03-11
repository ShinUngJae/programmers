def solution(num_list, n) :
    temp = []
    answer = []
    for i in range(len(num_list)) :
        temp.append(num_list[i])
        if (i + 1) % n == 0 :
            answer.append(temp)
            temp = []
    return answer


# 다른 사람의 풀이
# 풀이 1
def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        answer.append(num_list[i:i+n])
    return answer

# 풀이 2
def solution(num_list, n):
    return [num_list[ix-n:ix] for ix in range(n, len(num_list)+1, n)]