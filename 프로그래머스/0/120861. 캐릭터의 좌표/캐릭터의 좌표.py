def solution(keyinput, board):
    position = [0,0]
    a,b =board[0]//2,board[1]//2
    for i in keyinput:
        if i == 'left':
            if position[0] != -a:
                position[0] -= 1
        if i == 'right':
            if position[0] != a:
                position[0] += 1
        if i == 'up':
            if position[1] != b:
                position[1] +=1
        if i == 'down':
            if position[1] != -b:
                position[1] -= 1
    return position