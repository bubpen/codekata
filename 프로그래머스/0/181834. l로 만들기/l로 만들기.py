def solution(myString):
    answer = ''
    for i in myString:
        if ord(i) < ord('l'):
            answer = answer + 'l'
        else:
            answer = answer + i
    return answer