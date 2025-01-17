def solution(k, score):
    answer = []
    result = []
    for s in score:
        answer.append(s)
        if len(answer) > k:
            answer.sort(reverse = True)
            answer.pop()
        result.append(min(answer))
    return result