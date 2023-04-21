def solution(n, left, right):

    array = [[i + 1 if i > j else j + 1 for i in range(n)] for j in range(left // n, right // n + 1)]
    array2 = sum(array, [])
    
    return array2[left % n : (right // n - left // n) * n + right % n + 1]


# 다른 사람의 풀이
# 풀이 1
def solution(n, left, right):
    answer = []
    for i in range(left,right+1):
        answer.append(max(i//n,i%n)+1)
    return answer

# 풀이 2
def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        q, r = divmod(i, n)
        answer.append(max(q, r) + 1)

    return answer