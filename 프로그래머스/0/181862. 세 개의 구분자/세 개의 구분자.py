def solution(myStr):
    answer = []
    a = ''
    for w in range(len(myStr)):
        if myStr[w] == 'a' or myStr[w] == 'b' or myStr[w] == 'c':
            if a == '':
                pass
            else:
                answer.append(a)
                a = ''
        else:
            a = a + myStr[w]
            if w == len(myStr) -1:
                if a != '':
                    answer.append(a)
    if len(answer) == 0:
        answer.append('EMPTY')
    return answer