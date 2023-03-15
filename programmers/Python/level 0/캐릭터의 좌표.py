def solution(keyinput, board):
    width = board[0] // 2
    height = board[1] // 2
    answer = [0, 0]
    
    for i in keyinput :
        if i == "left" :
            answer[0] -= 1
        elif i == "right" :
            answer[0] += 1
        elif i == "up" :
            answer[1] += 1
        else :
            answer[1] -= 1
    
        if answer[0] < -width :
            answer[0] += 1
        elif answer[0] > width :
            answer[0] -= 1
        elif answer[1] < -height :
            answer[1] += 1
        elif answer[1] > height :
            answer[1] -= 1
    
    return answer


# 다른 사람의 코드
def solution(keyinput, board):
    x_lim,y_lim = board[0]//2,board[1]//2
    move = {'left':(-1,0),'right':(1,0),'up':(0,1),'down':(0,-1)}
    x,y = 0,0
    for k in keyinput:
        dx,dy = move[k]
        if abs(x+dx)>x_lim or abs(y+dy)>y_lim:
            continue
        else:
            x,y = x+dx,y+dy

    return [x,y]