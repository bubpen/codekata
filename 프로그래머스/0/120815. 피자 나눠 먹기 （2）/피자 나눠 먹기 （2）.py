def solution(n):
    answer = 1
    number = 1
    for i in range(1, n+1):
        if number * 6 % n == 0:
            answer = number
        else:
            number += 1
    return answer