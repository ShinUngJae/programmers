def solution(quiz):
    answer = []
    for i in quiz :
        temp = i.split(" = ")
        if eval(temp[0]) == int(temp[1]) :
            answer.append('O')
        else :
            answer.append('X')
    return answer


# 다른 사람의 풀이
def valid(equation):
    equation = equation.replace('=', '==')
    return eval(equation)

def solution(equations):
    return ["O" if valid(equation) else "X" for equation in equations]   