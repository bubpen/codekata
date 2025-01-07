def solution(t, p):
    answer = 0
    diff = len(p) -1
    for i in range(len(t) - diff):
        if int(t[i:i+len(p)]) <= int(p):
            answer += 1
    return answer