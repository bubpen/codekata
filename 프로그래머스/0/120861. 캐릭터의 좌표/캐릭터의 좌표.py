def solution(keyinput, board):
    position = [0,0]
    a,b =board[0]//2,board[1]//2
    for key in keyinput:
        if key == 'left':
            if position[0] != -a:
                position[0] -= 1
        if key == 'right':
            if position[0] != a:
                position[0] += 1
        if key == 'up':
            if position[1] != b:
                position[1] +=1
        if key == 'down':
            if position[1] != -b:
                position[1] -= 1
    return position