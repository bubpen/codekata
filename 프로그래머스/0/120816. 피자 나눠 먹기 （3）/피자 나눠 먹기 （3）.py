def solution(slice, n):
    number = 1
    answer = 1
    while (slice * number - n) < 0:
            number += 1
    return number