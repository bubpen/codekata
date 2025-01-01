def solution(s):
    l = list(map(int,s.split()))
    a, b = max(l), min(l)
    answer = []
    answer.append(str(b))
    answer.append(str(a))
    answer = ' '.join(answer)
    return answer