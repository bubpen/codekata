def solution(t, p):
    answer = 0
    diff = len(p) -1
    for i in range(len(t) - diff):
        num = ''
        for j in range(len(p)):
            num = num + t[i+j]
        if int(num) <= int(p):
            answer += 1
    return answer