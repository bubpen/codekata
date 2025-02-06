def solution(number, limit, power):
    answer = 0
    for n in range(1,number+1):
        div = 0
        for i in range(1, int(n**(1/2))+1):
            if n % i == 0:
                div += 1
                if n//i != i:
                    div += 1
        if div > limit:
            answer += power
        else:
            answer += div
    return answer