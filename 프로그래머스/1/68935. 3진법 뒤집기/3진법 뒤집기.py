def solution(n):
    answer = ''
    while n > 2:
        answer = answer + str(n % 3)
        n = n // 3
    answer = answer + str(n % 3)
    result = 0
    l = len(answer) -1
    for w in answer:
        result += int(w) * (3**l)
        l -= 1
    return result