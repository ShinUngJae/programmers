def solution(n):
    return sum([int(i) for i in str(n)])


# 다른 사람의 코드
def solution(n):
   answer = sum(list(map(int,list(str(n)))))
   return answer