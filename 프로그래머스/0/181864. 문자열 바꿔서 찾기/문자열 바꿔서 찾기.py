def solution(myString, pat):
    answer = 0
    change = ''
    for i in myString:
        if i == 'A':
            change = change + 'B'
        elif i == 'B':
            change = change + 'A'
    if pat in change:
        answer = 1
    return answer