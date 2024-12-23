def solution(a, b):
    M = max(a,b)
    m = min(a,b)
    answer = 0
    for i in range(m,M+1):
        answer += i
    return answer