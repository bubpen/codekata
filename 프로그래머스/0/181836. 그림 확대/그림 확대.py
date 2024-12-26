def solution(picture, k):
    answer = []
    for i in range(len(picture)*k):
        answer.append('')
    for i in range(len(answer)):
        for s in picture[i//k]:
            for n in range(k):
                answer[i] = answer[i] + s
    return answer