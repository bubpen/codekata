def solution(keyinput, board):
    p = [0,0]
    a,b =board[0]//2,board[1]//2
    for i in keyinput:
        if i == 'left':
            if p[0] != -a:
                p[0] -= 1
        if i == 'right':
            if p[0] != a:
                p[0] += 1
        if i == 'up':
            if p[1] != b:
                p[1] +=1
        if i == 'down':
            if p[1] != -b:
                p[1] -= 1
    return p