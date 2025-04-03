def solution(board, h, w):
    answer = 0
    m = len(board)-1
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    for i in range(4):
        check_h = h + dh[i]
        check_w = w + dw[i]
        check_h = min(check_h, m)
        check_h = max(check_h, 0)
        check_w = min(check_w, m)
        check_w = max(check_w, 0)
        if w == check_w and h == check_h:
            continue
        if board[h][w] == board[check_h][check_w]:
            answer += 1
    return answer