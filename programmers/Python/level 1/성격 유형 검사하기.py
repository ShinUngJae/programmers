def solution(survey, choices):
    answer = ''
    survey_dict = {i : 0 for i in ["R", "T", "C", "F", "J", "M", "A", "N"]}
    for i in range(len(survey)) :
        if  choices[i] < 4 :
            survey_dict[survey[i][0]] += 4 - choices[i]
        elif choices[i] > 4 :
            survey_dict[survey[i][1]] += choices[i] - 4
        print(survey_dict)
    
    if survey_dict["R"] >= survey_dict["T"] :
        answer += "R"
    else :
        answer += "T"
        
    if survey_dict["C"] >= survey_dict["F"] :
        answer += "C"
    else :
        answer += "F"
        
    if survey_dict["J"] >= survey_dict["M"] :
        answer += "J"
    else :
        answer += "M"
        
    if survey_dict["A"] >= survey_dict["N"] :
        answer += "A"
    else :
        answer += "N"
    
    return answer


# 다른 사람의 풀이
def solution(survey, choices):

    my_dict = {"RT":0,"CF":0,"JM":0,"AN":0}
    for A,B in zip(survey,choices):
        if A not in my_dict.keys():
            A = A[::-1]
            my_dict[A] -= B-4
        else:
            my_dict[A] += B-4

    result = ""
    for name in my_dict.keys():
        if my_dict[name] > 0:
            result += name[1]
        elif my_dict[name] < 0:
            result += name[0]
        else:
            result += sorted(name)[0]

    return result