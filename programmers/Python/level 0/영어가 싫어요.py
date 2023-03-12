import re

def solution(numbers):
    
    numbers = re.sub('one', '1', numbers)
    numbers = re.sub('two', '2', numbers)
    numbers = re.sub('three', '3', numbers)
    numbers = re.sub('four', '4', numbers)
    numbers = re.sub('five', '5', numbers)
    numbers = re.sub('six', '6', numbers)
    numbers = re.sub('seven', '7', numbers)
    numbers = re.sub('eight', '8', numbers)
    numbers = re.sub('nine', '9', numbers)
    numbers = re.sub('zero', '0', numbers)
    return int(numbers)


# 다른 사람의 코드
# 풀이 1
def solution(numbers):
    for num, eng in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        numbers = numbers.replace(eng, str(num))
    return int(numbers)

# 풀이 2
def solution(numbers):
    r = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',\
         'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    for k in r.keys():
        numbers = numbers.replace(k, r[k])

    return int(numbers)