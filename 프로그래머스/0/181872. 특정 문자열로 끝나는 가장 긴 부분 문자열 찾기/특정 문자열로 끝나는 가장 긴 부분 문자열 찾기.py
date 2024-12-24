def solution(myString, pat):
    answer = ''
    c = myString.count(pat)
    for i in myString:
        if answer.count(pat) == c:
            break
        else:
            answer = answer + i
    return answer