# 다른 사람의 풀이
def solution(s):
    answer = True
    stack = []
    for b in s:
        if b == '(':
            stack.append(b)
        elif len(stack) and b == ')':
            stack.pop()
        else:
            return False

    return False if len(stack) else True

# 내 풀이
# stack을 이용했지만, while문 사용과 위와 같이 for문을 더 효과적으로 이용하지 못했기 때문에 효율성 테스트에서 막힘