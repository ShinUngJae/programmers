def solution(s):
    answer = []
    s_dict = {}
    for i in range(len(s)) :
        if s[i] not in s_dict.keys() :
            s_dict[s[i]] = i
            answer.append(-1)
        else :
            answer.append(i - s_dict[s[i]])
            s_dict[s[i]] = i
    return answer