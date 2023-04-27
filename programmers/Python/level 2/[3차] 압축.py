from collections import deque

def solution(msg):
    
    msg = deque([i for i in msg])
    alpha = [chr(i) for i in range(65, 91)]
    alpha_dict = {i : j for i, j in zip(alpha, range(1, 27))}
    num = 26
    answer = []
    temp = ""

    while msg :
        temp += msg.popleft()
        if temp not in alpha_dict.keys() :
            num += 1
            alpha_dict[temp] = num
            answer.append(alpha_dict[temp[:-1]])
            temp = temp[-1]

    answer.append(alpha_dict[temp])
    return answer


# 다른 사람의 풀이
# 풀이 1
def solution(msg):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    d = {k:v for (k,v) in zip(alphabet, list(range(1,27)))}
    answer = []

    while True:
        if msg in d:
            answer.append(d[msg])
            break
        for i in range(1, len(msg)+1):
            if msg[0:i] not in d:
                answer.append(d[msg[0:i-1]])
                d[msg[0:i]] = len(d)+1
                msg = msg[i-1:]
                break

    return answer