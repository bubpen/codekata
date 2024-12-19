def solution(l, r):
    answer = []
    for i in range(l, r+1):
        for w in str(i):
            t = True
            if w in '12346789':
                t = False
                break    
        if t:
            answer.append(i)
    if len(answer) == 0:
        answer.append(-1)
    return answer