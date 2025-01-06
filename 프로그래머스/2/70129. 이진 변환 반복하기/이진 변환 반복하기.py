def solution(s):
    answer = []
    cnt = 0
    zeros = 0
    while s != '1':
        cnt += 1
        if '0' in s:
            zeros += s.count('0')
            s = s.replace('0','')
        if s == '1':
            break
        n = len(s)
        b = ''
        while n > 1:
            b = str(n % 2) + b
            n = n//2
            if n == 1:
                b = str(n % 2) + b
        s = b
    answer.append(cnt)
    answer.append(zeros)
    return answer