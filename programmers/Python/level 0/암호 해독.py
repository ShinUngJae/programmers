def solution(cipher, code):
    return ''.join([cipher[i] for i in range(len(cipher)) if (i + 1) % code == 0])


# 다른 사람의 풀이
def solution(cipher, code):
    answer = cipher[code-1::code]
    return answer