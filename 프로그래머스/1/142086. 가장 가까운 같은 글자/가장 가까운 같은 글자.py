def solution(s):
    answer = []
    for i, value in enumerate(s):
        if value in s[:i]:
            answer.append(s[i-1::-1].index(value)+1)
        else:
            answer.append(-1)
    return answer