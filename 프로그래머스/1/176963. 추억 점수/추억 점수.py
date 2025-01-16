def solution(name, yearning, photo):
    p = len(photo)
    answer = [0]*p
    n = len(name)
    for i in range(p):
        for j in range(n):
            if name[j] in photo[i]:
                answer[i] += yearning[j]
    return answer