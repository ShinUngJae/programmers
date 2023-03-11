def solution(s):
    s_list = s.split(" ")
    answer = []
    for i in range(len(s_list)) :
      if i == 0 :
        answer.append(int(s_list[i]))
      elif (s_list[i] == 'Z') :
        answer.pop()
      else :
          answer.append(int(s_list[i]))
    return sum(answer)


# 다른 사람의 코드
def solution(s):
    stack = []
    for a in s.split():
        if a != 'Z':
            stack.append(int(a))
        else:
            if stack:
                stack.pop()

    return sum(stack)