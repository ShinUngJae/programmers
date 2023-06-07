str1, str2 = input().strip().split(' ')
str3 = "".join([str1, str2])
print(str3)


# 다른 사람의 풀이
# 풀이 1
print(input().strip().replace(' ', ''))

# 풀이 2
str1, str2 = input().strip().split(' ')
print(str1 + str2)

# 풀이 3
str1, str2 = input().strip().split(' ')
print(str1, str2, sep='')