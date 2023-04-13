def solution(name, yearning, photo):
    name_list = {i : j for i, j in zip(name, yearning)}
    result = []
    for i in photo :
        score = 0
        for j in i :
            if j in name :
                score += name_list[j]
        result.append(score)
        
    return result