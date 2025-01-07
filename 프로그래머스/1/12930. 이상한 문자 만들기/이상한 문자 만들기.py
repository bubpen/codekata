def solution(s):
    answer = []
    w = ''
    for i in s.split(' '):
        for j in range(len(i)):
            if j % 2 == 0:
                w = w + i[j].upper()
            else:
                w = w + i[j].lower()
        answer.append(w)
        w = ''
    return ' '.join(answer)