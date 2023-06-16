a = int(input())
if a % 2 == 0 :
    print(a, "is even")
else :
    print(a, "is odd")


# 다른 사람의 풀이
N = int(input())
print(f"{N} is {'even' if N % 2 == 0 else 'odd'}")