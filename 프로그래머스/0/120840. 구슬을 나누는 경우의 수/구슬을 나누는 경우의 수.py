def solution(balls, share):
    a = 1
    for i in range(1,balls+1):
        a *= i
    b = 1
    for i in range(1,share+1):
        b *= i
    c = 1
    for i in range(1,balls-share+1):
        c *= i
    answer = a//(c*b)
    return answer