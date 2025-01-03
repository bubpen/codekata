def solution(s):
    answer = ''
    for i in range(len(s)):
        if i == 0:
            answer = answer + s[i].upper()
        else:
            if s[i-1] == ' ':
                answer = answer + s[i].upper()
            else:
                answer = answer + s[i].lower()
    return answer