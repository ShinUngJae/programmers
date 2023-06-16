def solution(myString):
    return "".join([i.upper() if i in ["a", "A"] else i.lower() for i in myString])


# 다른 사람의 풀이
def solution(myString):
    return myString.lower().replace('a', 'A')