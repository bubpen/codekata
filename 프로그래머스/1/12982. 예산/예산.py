def solution(d, budget):
    answer = 0
    d.sort()
    for dep in d:
        budget -= dep
        if budget < 0:
            break
        else:
            answer += 1
    return answer