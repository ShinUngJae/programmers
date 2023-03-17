import re

def solution(polynomial):
    polynomial = " " + polynomial
    poly = re.sub("([^0-9])(x)", " 1x", polynomial)
    poly_list = poly.split("+")
    poly_list = [re.sub(" ", "", i) for i in poly_list]
    x_value = 0
    num_value = 0
    
    for i in poly_list :
        if "x" in i :
            x_value += int(i[:-1])
        else :
            num_value += int(i)
            
    if x_value == 1 :
        x_value = "x"
    elif x_value > 1 :
        x_value = str(x_value) + "x"
    
    if x_value == 0 :
        answer = str(num_value)
    elif num_value == 0 :
        answer = x_value
    else :
        answer = x_value + " + " + str(num_value)
        
    return answer


# 다른 사람의 풀이
def solution(polynomial):
    xnum = 0
    const = 0
    for c in polynomial.split(' + '):
        if c.isdigit():
            const+=int(c)
        else:
            xnum = xnum+1 if c=='x' else xnum+int(c[:-1])
    if xnum == 0:
        return str(const)
    elif xnum==1:
        return 'x + '+str(const) if const!=0 else 'x'
    else:
        return f'{xnum}x + {const}' if const!=0 else f'{xnum}x'