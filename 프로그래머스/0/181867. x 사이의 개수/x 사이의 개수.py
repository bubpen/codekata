def solution(myString):
    answer = [0]
    for i in myString:
        if i == 'x':
            answer.append(0)
        else:
            answer[len(answer)-1] += 1
    return answer