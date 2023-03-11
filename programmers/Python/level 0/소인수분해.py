def aristo(k) :
    aristo_list = [True] * (k + 1)
    aristo_list[0], aristo_list[1] = False, False
    for i in range(2, (int(k ** 0.5) + 1)) :
        if aristo_list[i] == True :
            for j in range(i + i, k + 1, i) :
                aristo_list[j] = False
    return aristo_list

def solution(n):
    return [i for i in range(2, (n + 1)) if (n % i == 0) & (aristo(n)[i])]