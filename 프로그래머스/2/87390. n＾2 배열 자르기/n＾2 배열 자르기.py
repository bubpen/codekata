def solution(n, left, right):
    answer = []
    i = left // n
    j = left % n
    while len(answer) < right-left +1:
        answer.append(max(i+1,j+1))
        j += 1
        if j == n:
            i+=1
            j = 0
    return answer