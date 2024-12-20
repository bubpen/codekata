def solution(myString):
    answer = []
    a = ''
    for i in range(len(myString)):
        if myString[i] == 'x':
            if a == '':
                pass
            else:
                answer.append(a)
                a = ''
        else:
            if myString[i] == ' ':
                if i == len(myString) - 1:
                    if a != '':
                        answer.append(a)
                else:
                    pass
            else:
                if i == len(myString) -1:
                    a = a + myString[i]
                    answer.append(a)
                else:
                    a = a + myString[i]
    answer.sort()
    return answer