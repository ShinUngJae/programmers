from collections import Counter

def solution(array):
    array_Counter = Counter(array)
    array2 = array_Counter.most_common()
    
    if (len(array2) == 1) :
        return array2[0][0]
    elif (array2[0][1] > array2[1][1]) :
        return array2[0][0]
    else :
        return -1
    

# 다른 사람의 풀이
def solution(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            array.remove(a)
        if i == 0: return a
    return -1