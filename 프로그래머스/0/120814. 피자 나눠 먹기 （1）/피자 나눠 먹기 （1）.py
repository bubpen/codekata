def solution(n):
    number = 1
    answer = 1
    while n - 7*number > 0:
        if n - 7*number > 7:
            number += 1
            continue
        elif n - 7*number > 0:
            answer = number + 1
        else:
            answer = number
        number += 1
    return answer