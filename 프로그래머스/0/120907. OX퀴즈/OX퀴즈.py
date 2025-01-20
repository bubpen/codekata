def solution(quiz):
    answer = []
    for string in quiz:
        s = string.split()
        if s[1] =='+':
            if int(s[0]) + int(s[2]) == int(s[4]):
                answer.append("O")
            else:
                answer.append("X")
        if s[1] == '-':
            if int(s[0]) - int(s[2]) == int(s[4]):
                answer.append("O")
            else:
                answer.append("X")
    return answer