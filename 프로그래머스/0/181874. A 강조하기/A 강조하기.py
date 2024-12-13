def solution(myString):
    answer = ''
    for i in myString:
        if i in 'aA':
            answer = answer + 'A'
        else:
            answer = answer + i.lower()
    return answer