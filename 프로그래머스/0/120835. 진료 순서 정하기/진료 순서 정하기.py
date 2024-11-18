def solution(emergency):
    e = sorted(emergency, reverse = True)
    answer = []
    for i in emergency:
        answer.append(e.index(i)+1)
    return answer