def solution(hp):
    a = 0
    b = 0
    c = 0
    n = a+b+c
    while hp - (5*a + 3*b + c) > 0:
        if hp - (5*a + 3*b + c) >= 5:
            a += 1
        elif hp - (5*a + 3*b + c) >= 3:
            b += 1
        else:
            c += 1
        
    n = a+b+c
    return n