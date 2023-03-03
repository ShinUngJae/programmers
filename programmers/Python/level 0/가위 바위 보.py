def solution(rsp):
    RSP_dict = {'0' : '5', '2' : '0', '5' : '2'}
    answer = ''
    for i in rsp :
        answer += RSP_dict[i]
    return answer