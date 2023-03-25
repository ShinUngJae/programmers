def solution(keymap, targets):
    answer = []
    for i in targets :
        temp = 0
        for j in range(len(i)) :
            if i[j] not in "".join(keymap) :
                temp = -1
                break
            else :
                temp2 = len("".join(keymap))
                for k in range(len(keymap)) :
                    if keymap[k].find(i[j]) > -1 :
                        temp2 = min(temp2, keymap[k].find(i[j]))
                temp += temp2 + 1
        answer.append(temp)
    return answer


# 다른 사람의 풀이
def solution(keymap, targets):
    answer = []
    hs = {}
    for k in keymap:
        for i, ch in enumerate(k):
            hs[ch] = min(i + 1, hs[ch]) if ch in hs else i + 1

    for i, t in enumerate(targets):
        ret = 0
        for ch in t:
            if ch not in hs:
                ret = - 1
                break
            ret += hs[ch]
        answer.append(ret)

    return answer