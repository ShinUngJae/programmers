def solution(arr, k):
    return [i * k for i in arr] if k % 2 == 1 else [i + k for i in arr]


# 다른 사람의 풀이
# 풀이 1
def solution(arr, k):
    if k % 2 != 0:
        return list(map(lambda x: x * k, arr))

    return list(map(lambda x: x + k, arr))

# 풀이 2
def solution(arr, k):
    return [i*k if k%2!=0 else i+k for i in arr]