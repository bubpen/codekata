def solution(money):
    n = 1
    if money - 5500 * n >= 0:
        while money - 5500 * n >= 0:
            n += 1
    answer = []
    if money - 5500 * n> 0:
        answer.append(n)
        answer.append(money - 5500 * n)
    else:
        answer.append(n-1)
        answer.append(money - 5500 * (n-1))
    return answer