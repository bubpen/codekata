def solution(n):
    answer = []
    i = 2
    while i <= n:
        if n%i==0:
            if i not in answer:
                answer.append(i)
                n = n//i
            else:
                n = n//i
        else:
            i += 1
    return answer