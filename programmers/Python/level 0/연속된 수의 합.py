def solution(num, total) :
    temp = ((2 * total // num) - (num - 1)) // 2
    return [i for i in range(temp, temp + num)]