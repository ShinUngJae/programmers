def Date(date, term) :
    date_list = [int(i) for i in date.split(".")]
    date_list[1] += term
    date_list[2] -= 1

    if date_list[2] == 0 :
        date_list[2] = 28
        date_list[1] -= 1
    
    if date_list[1] > 12 :
        date_list[0] += date_list[1] // 12
        date_list[1] = date_list[1] % 12
    
    if date_list[1] == 0 :
        date_list[1] = 12
        date_list[0] -= 1
         
    date_list2 = []
    date_list2.append(str(date_list[0]))
    
    if date_list[1] < 10 :
        temp = "0" + str(date_list[1])
        date_list2.append(temp)
    else :
        date_list2.append(str(date_list[1]))
        
    if date_list[2] < 10 :
        temp = "0" + str(date_list[2])
        date_list2.append(temp)
    else :
        date_list2.append(str(date_list[2]))

    return ".".join([str(i) for i in date_list2])


def solution(today, terms, privacies):
    answer = []
    terms_dict = {i.split()[0] : i.split()[1] for i in terms}
    for j in range(len(privacies)) :
        j_term = int(terms_dict[privacies[j].split()[1]])

        if today > Date(privacies[j].split()[0], j_term) :
            answer.append(j + 1)
        print(today, Date(privacies[j].split()[0], j_term))

    return answer


# 다른 사람의 풀이
# 풀이 1
def to_days(date):
    year, month, day = map(int, date.split("."))
    return year * 28 * 12 + month * 28 + day

def solution(today, terms, privacies):
    months = {v[0]: int(v[2:]) * 28 for v in terms}
    today = to_days(today)
    expire = [
        i + 1 for i, privacy in enumerate(privacies)
        if to_days(privacy[:-2]) + months[privacy[-1]] <= today
    ]
    return expire