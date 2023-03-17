def solution(board):
    width = len(board)
    answer_board = [[0 for i in range(width)] for j in range(width)]
    for i in range(width) :
        for j in range(width) :
            if board[i][j] == 1 :
                temp = [[i - 1, j - 1], [i, j - 1], [i + 1, j - 1], [i + 1, j],
                       [i + 1, j + 1], [i, j + 1], [i - 1, j + 1], [i - 1, j], [i, j]]
                temp2 = [i for i in temp if (i[0] >= 0) & (i[0] < width) & (i[1] >= 0) & (i[1] < width)]
                for k in temp2 :
                    answer_board[k[0]][k[1]] = 1
    return width ** 2 - sum([sum(i) for i in answer_board])


# 다른 사람의 풀이
def solution(board):
    n = len(board)
    danger = set()
    for i, row in enumerate(board):
        for j, x in enumerate(row):
            if not x:
                continue
            danger.update((i+di, j+dj) for di in [-1,0,1] for dj in [-1, 0, 1])
    return n*n - sum(0 <= i < n and 0 <= j < n for i, j in danger)